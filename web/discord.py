import json
import time
from urllib.parse import urlencode

from config import DISCORD


class CONSTANTS:
    API_URL = "https://discord.com/api"
    AUTH_URL = "https://discord.com/api/oauth2/authorize"
    TOKEN_URL = "https://discord.com/api/oauth2/token"
    SCOPES = [
        "guilds",
        "guilds.join",
        "identify",
    ]


class Oauth:
    def __init__(self, bot_or_app):
        self.client_id = DISCORD.client_id
        self.client_secret = DISCORD.client_secret
        self.redirect_uri = DISCORD.redirect_uri
        self.scope = " ".join(CONSTANTS.SCOPES)

        self.client = bot_or_app

    def get_auth_url(self, invite=False):
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": self.scope + " bot applications.commands"
            if invite
            else self.scope,
            "prompt": "none",  # "consent" to force them to agree again
        }
        query_params = urlencode(params)
        return "%s?%s" % (CONSTANTS.AUTH_URL, query_params)

    def validate_token(self, token_info):
        """Checks a token is valid"""
        now = int(time.time())
        return token_info["expires_at"] - now > 60

    async def get_access_token(self, user):
        """Gets the token or creates a new one if expired"""
        if self.validate_token(user.token_info):
            return user.token_info["access_token"]

        user.token_info = await self.refresh_access_token(
            user.user_id, user.token_info.get("refresh_token")
        )

        return user.token_info["access_token"]

    async def refresh_access_token(self, user_id, refresh_token):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        token_info = await self.client.http_utils.post(
            CONSTANTS.TOKEN_URL, data=params, headers=headers, res_method="json"
        )
        token_info["expires_at"] = int(time.time()) + token_info["expires_in"]

        query = """
                INSERT INTO discord_auth
                VALUES ($1, $2)
                ON CONFLICT (user_id)
                DO UPDATE SET token_info = $2
                WHERE discord_auth.user_id = $1;
                """
        await self.client.cxn.execute(query, user_id, json.dumps(token_info))

        return token_info

    async def request_access_token(self, code):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code",
            "scope": self.scope,
            "code": code,
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        token_info = await self.client.http_utils.post(
            CONSTANTS.TOKEN_URL, data=params, headers=headers, res_method="json"
        )

        if not token_info.get("expires_in"):  # Something went wrong, return None
            return

        token_info["expires_at"] = int(time.time()) + token_info["expires_in"]
        return token_info

    async def identify(self, access_token):

        headers = {"Authorization": f"Bearer {access_token}"}

        user_data = await self.client.http_utils.get(
            url=CONSTANTS.API_URL + "/users/@me", headers=headers, res_method="json"
        )
        return user_data


class User:  # Discord user operations with scopes
    def __init__(self, token_info, user_id, bot_or_app, *, oauth=None):
        self.token_info = token_info
        self.user_id = user_id
        self.client = bot_or_app
        self.oauth = oauth or Oauth(bot_or_app)

    @classmethod
    async def from_id(cls, user_id, bot_or_app):
        query = """
                SELECT token_info
                FROM discord_auth
                WHERE user_id = $1;
                """
        token_info = await bot_or_app.cxn.fetchval(query, int(user_id))

        if token_info:
            token_info = json.loads(token_info)
            return cls(token_info, user_id)

    @classmethod
    async def from_token(cls, token_info, bot_or_app):
        oauth = Oauth(bot_or_app)
        user_data = await oauth.identify(token_info.get("access_token"))
        user_id = int(user_data.get("id"))
        query = """
                INSERT INTO discord_auth
                VALUES ($1, $2)
                ON CONFLICT (user_id)
                DO UPDATE SET token_info = $2
                WHERE discord_auth.user_id = $1;
                """
        await bot_or_app.cxn.execute(query, user_id, json.dumps(token_info))

        return cls(token_info, user_id, bot_or_app, oauth=oauth)

    async def get(self, url, *, access_token=None):
        access_token = access_token or await self.oauth.get_access_token(self)

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        return await self.client.http_utils.get(url, headers=headers, res_method="json")

    async def identify(self):
        return await self.get(CONSTANTS.API_URL + "/users/@me")

    async def get_guilds(self):
        return await self.get(CONSTANTS.API_URL + "/users/@me/guilds")

    async def join_guild(self, guild_id):
        access_token = await self.oauth.get_access_token(self)

        params = {"access_token": access_token}
        headers = {
            "Authorization": f"Bot {DISCORD.token}",
        }
        return await self.client.http_utils.put(
            CONSTANTS.API_URL + f"/guilds/{guild_id}/members/{self.user_id}",
            headers=headers,
            json=params,
        )
