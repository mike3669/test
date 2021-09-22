from utilities import utils

config = utils.config()
try:
    admins = config["admins"]
    bitly = config["bitly"]
    embed = config["embed"]
    gtoken = config["gtoken"]
    owners = config["owners"]
    postgres = config["postgres"]
    prefix = config["prefix"]
    support = config["support"]
    tester = config["tester"]
    timezonedb = config["timezonedb"]
    token = config["token"]
except KeyError as e:
    print(
        f"""
          Warning! The key {e} is missing from your ./config.json file.
          Add this key or the bot might not function properly.
          """
    )


class Colors(object):
    GREEN = (46, 204, 113)
    YELLOW = (255, 228, 0)
    RED = (237, 41, 57)
    GRAY = (97, 109, 126)
    BLUE = (10, 24, 34)
    WHITE = (255, 255, 255)
    PINK = (255, 196, 235)


emotes = {
    "loading": "<a:loading:875108637549408297>",
    "lightbulb": "<:help:866884635664187424>",
    "success": "<:checkmark:875108614904373289>",
    "failed": "<:failed:875140082598817873>",
    "warn": "<:warn:875108597208600637>",
    "error": "<:error:875108644633579571>",
    "announce": "<:announce:875108641420750878>",
    "1234button": "<:1234:875108607434301560>",
    "info": "<:info:827428282001260544>",
    "help": "<:help:889599139460034640>",
    "exclamation": "<:exclamation:827753511395000351>",
    "trash": "<:trash:875108609317560412>",
    "forward": "<:forward:875108604275990598>",
    "forward2": "<:forward2:875108599825834034>",
    "backward": "<:backward:875108605844684870>",
    "backward2": "<:backward2:875108602011058277>",
    "desktop": "<:desktop:875108626254143559>",
    "mobile": "<:mobile:875108628800077847>",
    "search": "<:web:875108630498775071>",
    "online": "<:online:875108662388076575>",
    "offline": "<:offline:875108660634857522>",
    "dnd": "<:dnd:875108655232581683>",
    "idle": "<:idle:875108657103257650>",
    "owner": "<:owner:850175556866932787>",
    "emoji": "<:emoji:875108595031748629>",
    "members": "<:members:875108593110765578>",
    "categories": "<:categories:875108590166360135>",
    "textchannel": "<:textchannel:875108586261454879>",
    "voicechannel": "<:voicechannel:875108588236972092>",
    "messages": "<:messages:875108620315033611>",
    "commands": "<:command:875108618645684274>",
    "role": "<:role:875108622311522375>",
    "invite": "<:invite:875108624303788032>",
    "bot": "<:bot:875108616745656370>",
    "question": "<:question:875108636022702190>",
    "lock": "<:lock:875108632650469478>",
    "unlock": "<:unlock:875108634294636574>",
    "letter": "<:letter:875108610991087697>",
    "num0": "<:num0:827219939583721513>",
    "num1": "<:num1:827219939961602098>",
    "num2": "<:num2:827219940045226075>",
    "num3": "<:num3:827219940541071360>",
    "num4": "<:num4:827219940556931093>",
    "num5": "<:num5:827219941253709835>",
    "num6": "<:num6:827219941790580766>",
    "num7": "<:num7:827219942343442502>",
    "num8": "<:num8:827219942444236810>",
    "num9": "<:num9:827219942758809610>",
    "stop": "<:stop:827257105420910652>",
    "stopsign": "<:stopsign:841848010690658335>",
    "clock": "<:clock:839640961755643915>",
    "alarm": "<:alarm:839640804246683648>",
    "stopwatch": "<:stopwatch:875108639126454293>",
    "log": "<:log:875108643253665832>",
    "db": "<:database:875108649750630470>",
    "privacy": "<:privacy:875108651206062101>",
    "delete": "<:deletedata:875108653483573311>",
    "heart": "<:heart:875108647200522310>",
    "graph": "<:graph:840046538340040765>",
    "upload": "<:upload:840086768497983498>",
    "download": "<:download:840086726209961984>",
    "right": "<:right:840289355057725520>",
    "left": "<:left:887824901912817664>",
    "kick": "<:kick:840490315893702667>",  # So its a she 💞
    "ban": "<:ban:840474680547606548>",
    "robot": "<:robot:840482243218767892>",
    "plus": "<:plus:840485455333294080>",
    "minus": "<:minus:840485608555020308>",
    "undo": "<:undo:840486528110166056>",
    "redo": "<:redo:840486303354322962>",
    "audioadd": "<:audioadd:840491464928002048>",
    "audioremove": "<:audioremove:840491410720948235>",
    "pin": "<:pin:840492943226961941>",
    "pass": "<:pass:840817730277867541>",
    "fail": "<:fail:840817815148953600>",
    "snowflake": "<:snowflake:841848061412376596>",
    "dev": "<:botdev:850169506310389820>",
    "user": "<:user:850173056140050442>",
    "join": "<:join:850175242009313342>",
    "leave": "<:leave:850175275316019220>",
    "nitro": "<:nitro:850175331197124618>",
    "staff": "<:staff:850175717131681842>",
    "partner": "<:partner:850175829182251058>",
    "boost": "<:boost:850175958505357343>",
    "balance": "<:balance:850176108099665920>",
    "brilliance": "<:brilliance:850176212537835530>",
    "bravery": "<:bravery:850176483136766013>",
    "moderator": "<:moderator:850176521154330637>",
    "bughuntergold": "<:bughuntergold:850176871751614514>",
    "bughunter": "<:bughunter:850176820976549899>",
    "supporter": "<:supporter:875108664304889866>",
    "hypesquad": "<:hypesquad:875108666083266610>",
    "like": "<:like:854215293048193034>",
    "dislike": "<:dislike:854215235005841418>",
    "youtube": "<:youtube:854214998770057226>",
    "pause": "<:pause:854214661481431080>",
    "play": "<:play:854216311014031360>",
    "music": "<:music:854216986719813634>",
    "volume": "<:volume:854216882567905302>",
    "skip": "<:skip:854216673803763732>",
    "previous": "<:prev:889615934950617109>",
    "rewind": "<:rewind:889697229579902976>",
    "fastforward": "<:fast:889697357158055947>",
    "wave": "<:wave:854218904033296414>",
    "loop": "<:loop:854254549488107561>",
    "shuffle": "<:shuffle:857063084854476840>",
    "redo": "<:redo:883511598822604850>",
    "github": "<:github:857675832432525342>",
    "admin": "<:admin:860645534423318579>",
    "web": "<:web:875108630498775071>",
    "dj": "<:dj:886121077082845184>",
    "speed": "<:speed:890340712086904852>",
    "clarinet": "<:clarinet:854217207248977930>",  # For me :)
}
progress_bars = [
    "https://cdn.discordapp.com/attachments/872338764276576266/889735911905034291/progress0.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735913003941898/progress1.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735914287423528/progress2.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735915545710652/progress3.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735916640436234/progress4.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735934139060285/progress5.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735935267340378/progress6.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735936311705600/progress7.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735937951666196/progress8.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735939071565824/progress9.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735956607950888/progress10.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735957711060992/progress11.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735958763823204/progress12.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735959900475412/progress13.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735961225867284/progress14.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735978988740628/progress15.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735980142198784/progress16.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735981966716948/progress17.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735983543758918/progress18.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889735984982396979/progress19.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736001570869278/progress20.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736002829180940/progress21.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736003982602280/progress22.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736005094101032/progress23.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736006348202004/progress24.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736025964957727/progress25.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736027902730290/progress26.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736029140025364/progress27.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736030234763275/progress28.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736031228788766/progress29.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736048026996776/progress30.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736049893474334/progress31.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736051051077662/progress32.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736052305178644/progress33.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736053500559360/progress34.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736069854142524/progress35.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736070936293416/progress36.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736072093892638/progress37.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736073205399602/progress38.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736074627268638/progress39.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736092490825798/progress40.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736094021738497/progress41.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736095808516096/progress42.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736097205215292/progress43.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736098803240960/progress44.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736114712240138/progress45.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736116066988042/progress46.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736118218653756/progress47.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736119598583868/progress48.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736120827527198/progress49.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736136820412476/progress50.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736138812690442/progress51.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736140423331880/progress52.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736142256209920/progress53.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736143883628574/progress54.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736158869860362/progress55.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736160182677534/progress56.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736161784901682/progress57.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736163148050432/progress58.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736164481830952/progress59.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736181393281054/progress60.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736183645630464/progress61.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736185969266718/progress62.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736187261120542/progress63.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736188934619187/progress64.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736203400794112/progress65.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736204755550248/progress66.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736206286467102/progress67.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736207880314890/progress68.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736209381879838/progress69.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736225567670282/progress70.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736227002130432/progress71.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736228545630218/progress72.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736229946531900/progress73.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736231464890428/progress74.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736248321781820/progress75.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736252163772447/progress76.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736255103979560/progress77.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736256643272724/progress78.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736257968676914/progress79.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736270270578718/progress80.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736271885389864/progress81.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736273525370880/progress82.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736275337289768/progress83.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736277019217940/progress84.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736292659789825/progress85.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736294073257994/progress86.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736295729995807/progress87.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736297403514911/progress88.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736299127382036/progress89.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736314721796136/progress90.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736316235943976/progress91.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736318026907679/progress92.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736319536877598/progress93.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736321302663238/progress94.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736337756921886/progress95.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736339380137994/progress96.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736340793593876/progress97.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736342546808852/progress98.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736344404901898/progress99.png",
    "https://cdn.discordapp.com/attachments/872338764276576266/889736359504408576/progress100.png",
]
profanities = [
    "anal",
    "anus",
    "areole",
    "arian",
    "arrse",
    "arse",
    "arsehole",
    "aryan",
    "asanchez",
    "ass",
    "assbang",
    "assbanged",
    "asses",
    "assfuck",
    "assfucker",
    "assfukka",
    "asshole",
    "assmunch",
    "asswhole",
    "autoerotic",
    "ballsack",
    "bastard",
    "bdsm",
    "beastial",
    "beastiality",
    "bellend",
    "bestial",
    "bestiality",
    "bimbo",
    "bimbos",
    "bitch",
    "bitches",
    "bitchin",
    "bitching",
    "blowjob",
    "blowjobs",
    "blue waffle",
    "bondage",
    "boner",
    "boob",
    "boobs",
    "booobs",
    "boooobs",
    "booooobs",
    "booooooobs",
    "booty call",
    "breasts",
    "brown shower",
    "brown showers",
    "buceta",
    "bukake",
    "bukkake",
    "bullshit",
    "busty",
    "butthole",
    "carpet muncher",
    "cawk",
    "chink",
    "cipa",
    "clit",
    "clitoris",
    "clits",
    "cnut",
    "cock",
    "cockface",
    "cockhead",
    "cockmunch",
    "cockmuncher",
    "cocks",
    "cocksuck",
    "cocksucked",
    "cocksucker",
    "cocksucking",
    "cocksucks",
    "cokmuncher",
    "coon",
    "cowgirl",
    "cowgirls",
    "crap",
    "crotch",
    "cum",
    "cuming",
    "cummer",
    "cumming",
    "cums",
    "cumshot",
    "cunilingus",
    "cunillingus",
    "cunnilingus",
    "cunt",
    "cuntlicker",
    "cuntlicking",
    "cunts",
    "damn",
    "deepthroat",
    "dick",
    "dickhead",
    "dildo",
    "dildos",
    "dink",
    "dinks",
    "dlck",
    "dog style",
    "dog-fucker",
    "doggiestyle",
    "doggin",
    "dogging",
    "doggystyle",
    "dong",
    "donkeyribber",
    "doofus",
    "doosh",
    "dopey",
    "douche",
    "douchebag",
    "douchebags",
    "douchey",
    "drunk",
    "duche",
    "dumass",
    "dumbass",
    "dumbasses",
    "dummy",
    "dyke",
    "dykes",
    "eatadick",
    "eathairpie",
    "ejaculate",
    "ejaculated",
    "ejaculates",
    "ejaculating",
    "ejaculatings",
    "ejaculation",
    "ejakulate",
    "enlargement",
    "erect",
    "erection",
    "erotic",
    "erotism",
    "essohbee",
    "extacy",
    "extasy",
    "facial",
    "fack",
    "fag",
    "fagg",
    "fagged",
    "fagging",
    "faggit",
    "faggitt",
    "faggot",
    "faggs",
    "fagot",
    "fagots",
    "fags",
    "faig",
    "faigt",
    "fanny",
    "fannybandit",
    "fannyflaps",
    "fannyfucker",
    "fanyy",
    "fart",
    "fartknocker",
    "fat",
    "fatass",
    "fcuk",
    "fcuker",
    "fcuking",
    "feck",
    "fecker",
    "felch",
    "felcher",
    "felching",
    "fellate",
    "fellatio",
    "feltch",
    "feltcher",
    "femdom",
    "fingerfuck",
    "fingerfucked",
    "fingerfucker",
    "fingerfuckers",
    "fingerfucking",
    "fingerfucks",
    "fingering",
    "fisted",
    "fistfuck",
    "fistfucked",
    "fistfucker",
    "fistfuckers",
    "fistfucking",
    "fistfuckings",
    "fistfucks",
    "fisting",
    "fisty",
    "flange",
    "flogthelog",
    "floozy",
    "foad",
    "fondle",
    "foobar",
    "fook",
    "fooker",
    "footjob",
    "foreskin",
    "freex",
    "frigg",
    "frigga",
    "fubar",
    "fuck",
    "fucka",
    "fuckass",
    "fuckbitch",
    "fucked",
    "fucker",
    "fuckers",
    "fuckface",
    "fuckhead",
    "fuckheads",
    "fuckhole",
    "fuckin",
    "fucking",
    "fuckings",
    "fuckingshitmotherfucker",
    "fuckme",
    "fuckmeat",
    "fucknugget",
    "fucknut",
    "fuckoff",
    "fuckpuppet",
    "fucks",
    "fucktard",
    "fucktoy",
    "fucktrophy",
    "fuckup",
    "fuckwad",
    "fuckwhit",
    "fuckwit",
    "fuckyomama",
    "fudgepacker",
    "fuk",
    "fuker",
    "fukker",
    "fukkin",
    "fukking",
    "fuks",
    "fukwhit",
    "fukwit",
    "futanari",
    "futanary",
    "fux",
    "fuxor",
    "fxck",
    "gae",
    "gai",
    "gangbang",
    "gangbanged",
    "gangbangs",
    "ganja",
    "gassyass",
    "gay",
    "gaylord",
    "gays",
    "gaysex",
    "gey",
    "gfy",
    "ghay",
    "ghey",
    "gigolo",
    "glans",
    "goatse",
    "god",
    "godamn",
    "godamnit",
    "goddam",
    "goddammit",
    "goddamn",
    "goddamned",
    "gokkun",
    "goldenshower",
    "gonad",
    "gonads",
    "gook",
    "gooks",
    "gringo",
    "gspot",
    "gtfo",
    "guido",
    "hamflap",
    "handjob",
    "hardcoresex",
    "hardon",
    "hebe",
    "heeb",
    "hell",
    "hemp",
    "hentai",
    "heroin",
    "herp",
    "herpes",
    "herpy",
    "heshe",
    "hitler",
    "hiv",
    "hoar",
    "hoare",
    "hobag",
    "hoer",
    "homey",
    "homo",
    "homoerotic",
    "homoey",
    "honky",
    "hooch",
    "hookah",
    "hooker",
    "hoor",
    "hootch",
    "hooter",
    "hooters",
    "hore",
    "horniest",
    "horny",
    "hotsex",
    "howtokill",
    "howtomurdep",
    "hump",
    "humped",
    "humping",
    "hussy",
    "hymen",
    "inbred",
    "incest",
    "injun",
    "jackass",
    "jackhole",
    "jackoff",
    "jap",
    "japs",
    "jerk",
    "jerked",
    "jerkoff",
    "jism",
    "jiz",
    "jizm",
    "jizz",
    "jizzed",
    "junkie",
    "junky",
    "kawk",
    "kike",
    "kikes",
    "kill",
    "kinbaku",
    "kinky",
    "kinkyJesus",
    "kkk",
    "klan",
    "knob",
    "knobead",
    "knobed",
    "knobend",
    "knobhead",
    "knobjocky",
    "knobjokey",
    "kock",
    "kondum",
    "kondums",
    "kooch",
    "kooches",
    "kootch",
    "kraut",
    "kum",
    "kummer",
    "kumming",
    "kums",
    "kunilingus",
    "kwif",
    "kyke",
    "l3itch",
    "labia",
    "lech",
    "leper",
    "lesbians",
    "lesbo",
    "lesbos",
    "lez",
    "lezbian",
    "lezbians",
    "lezbo",
    "lezbos",
    "lezzie",
    "lezzies",
    "lezzy",
    "lmao",
    "lmfao",
    "loin",
    "loins",
    "lube",
    "lust",
    "lusting",
    "lusty",
    "m-fucking",
    "mafugly",
    "mams",
    "masochist",
    "massa",
    "masterb8",
    "masterbate",
    "masterbating",
    "masterbation",
    "masterbations",
    "masturbate",
    "masturbating",
    "masturbation",
    "maxi",
    "menses",
    "menstruate",
    "menstruation",
    "meth",
    "milf",
    "mofo",
    "molest",
    "moolie",
    "moron",
    "mothafuck",
    "mothafucka",
    "mothafuckas",
    "mothafuckaz",
    "mothafucked",
    "mothafucker",
    "mothafuckers",
    "mothafuckin",
    "mothafucking",
    "mothafuckings",
    "mothafucks",
    "motherfuck",
    "motherfucka",
    "motherfucked",
    "motherfucker",
    "motherfuckers",
    "motherfuckin",
    "motherfucking",
    "motherfuckings",
    "motherfuckka",
    "motherfucks",
    "mtherfucker",
    "mthrfucker",
    "mthrfucking",
    "muff",
    "muffdiver",
    "muffpuff",
    "murder",
    "mutha",
    "muthafecker",
    "muthafuckaz",
    "muthafucker",
    "muthafuckker",
    "muther",
    "mutherfucker",
    "mutherfucking",
    "muthrfucking",
    "nad",
    "nads",
    "naked",
    "napalm",
    "nappy",
    "nazi",
    "nazism",
    "needthedick",
    "negro",
    "nig",
    "nigg",
    "nigga",
    "niggah",
    "niggas",
    "niggaz",
    "nigger",
    "niggers",
    "niggle",
    "niglet",
    "nimrod",
    "ninny",
    "nipple",
    "nipples",
    "nob",
    "nobhead",
    "nobjocky",
    "nobjokey",
    "nooky",
    "nude",
    "nudes",
    "numbnuts",
    "nutbutter",
    "nutsack",
    "nympho",
    "omg",
    "opiate",
    "opium",
    "oral",
    "orally",
    "organ",
    "orgasim",
    "orgasims",
    "orgasm",
    "orgasmic",
    "orgasms",
    "orgies",
    "orgy",
    "ovary",
    "ovum",
    "ovums",
    "paddy",
    "paki",
    "pantie",
    "panties",
    "panty",
    "pastie",
    "pasty",
    "pawn",
    "pcp",
    "pecker",
    "pedo",
    "pedophile",
    "pedophilia",
    "pedophiliac",
    "pee",
    "peepee",
    "penetrate",
    "penetration",
    "penial",
    "penile",
    "penis",
    "penisfucker",
    "perversion",
    "peyote",
    "phalli",
    "phallic",
    "phonesex",
    "phuck",
    "phuk",
    "phuked",
    "phuking",
    "phukked",
    "phukking",
    "phuks",
    "phuq",
    "pigfucker",
    "pillowbiter",
    "pimp",
    "pimpis",
    "pinko",
    "piss",
    "pissed",
    "pisser",
    "pissers",
    "pisses",
    "pissflaps",
    "pissin",
    "pissing",
    "pissoff",
    "playboy",
    "pms",
    "polack",
    "pollock",
    "poon",
    "poontang",
    "poop",
    "porn",
    "porno",
    "pornography",
    "pornos",
    "pot",
    "potty",
    "prick",
    "pricks",
    "prig",
    "pron",
    "prostitute",
    "prude",
    "pube",
    "pubic",
    "pubis",
    "punkass",
    "punky",
    "puss",
    "pusse",
    "pussi",
    "pussies",
    "pussy",
    "pussyfart",
    "pussypalace",
    "pussypounder",
    "pussys",
    "puto",
    "queaf",
    "queef",
    "queer",
    "queero",
    "queers",
    "quicky",
    "quim",
    "racy",
    "rape",
    "raped",
    "raper",
    "raping",
    "rapist",
    "raunch",
    "rectal",
    "rectum",
    "rectus",
    "reefer",
    "reetard",
    "reich",
    "retard",
    "retarded",
    "revue",
    "rimjaw",
    "rimjob",
    "rimming",
    "ritard",
    "rtard",
    "rum",
    "rump",
    "rumprammer",
    "ruski",
    "sadism",
    "sadist",
    "sandbar",
    "sausagequeen",
    "scag",
    "scantily",
    "schizo",
    "schlong",
    "screw",
    "screwed",
    "screwing",
    "scroat",
    "scrog",
    "scrot",
    "scrote",
    "scrotum",
    "scrud",
    "scum",
    "seaman",
    "seamen",
    "seduce",
    "semen",
    "sex",
    "sexual",
    "shag",
    "shagger",
    "shaggin",
    "shagging",
    "shamedame",
    "shemale",
    "shibari",
    "shibary",
    "shit",
    "shitdick",
    "shite",
    "shiteater",
    "shited",
    "shitey",
    "shitface",
    "shitfuck",
    "shitfucker",
    "shitfull",
    "shithead",
    "shithole",
    "shithouse",
    "shiting",
    "shitings",
    "shits",
    "shitt",
    "shitted",
    "shitter",
    "shitters",
    "shitting",
    "shittings",
    "shitty",
    "shiz",
    "shota",
    "sissy",
    "skag",
    "skank",
    "slave",
    "sleaze",
    "sleazy",
    "slope",
    "slut",
    "slutbucket",
    "slutdumper",
    "slutkiss",
    "sluts",
    "smegma",
    "smut",
    "smutty",
    "snatch",
    "sniper",
    "snuff",
    "sob",
    "sodom",
    "son-of-a-bitch",
    "souse",
    "soused",
    "spac",
    "sperm",
    "spic",
    "spick",
    "spik",
    "spiks",
    "spooge",
    "spunk",
    "steamy",
    "stfu",
    "stiffy",
    "stoned",
    "strip",
    "strip club",
    "stripclub",
    "stroke",
    "stupid",
    "suck",
    "sucked",
    "sucking",
    "sumofabiatch",
    "tampon",
    "tard",
    "tawdry",
    "teabagging",
    "teat",
    "teets",
    "teez",
    "terd",
    "teste",
    "testee",
    "testes",
    "testical",
    "testicle",
    "testis",
    "threesome",
    "throating",
    "thrust",
    "thug",
    "tinkle",
    "tit",
    "titfuck",
    "titi",
    "tits",
    "titt",
    "tittiefucker",
    "titties",
    "titty",
    "tittyfuck",
    "tittyfucker",
    "tittywank",
    "titwank",
    "toke",
    "toots",
    "tosser",
    "tramp",
    "transsexual",
    "trashy",
    "tubgirl",
    "turd",
    "tush",
    "twat",
    "twathead",
    "twats",
    "twatty",
    "twunt",
    "twunter",
    "ugly",
    "undies",
    "unwed",
    "urinal",
    "urine",
    "uterus",
    "uzi",
    "vag",
    "vagina",
    "valium",
    "viagra",
    "vigra",
    "virgin",
    "vixen",
    "vodka",
    "vomit",
    "voyeur",
    "vulgar",
    "vulva",
    "wad",
    "wang",
    "wank",
    "wanker",
    "wanky",
    "wazoo",
    "wedgie",
    "weed",
    "weenie",
    "weewee",
    "weiner",
    "weirdo",
    "wench",
    "wetback",
    "whitey",
    "whiz",
    "whoar",
    "whoralicious",
    "whore",
    "whorealicious",
    "whored",
    "whoreface",
    "whorehopper",
    "whorehouse",
    "whores",
    "whoring",
    "wigger",
    "willies",
    "willy",
    "womb",
    "woody",
    "woose",
    "wop",
    "wtf",
    "x-rated2g1c",
    "xx",
    "xxx",
    "yaoi",
    "yury",
]
