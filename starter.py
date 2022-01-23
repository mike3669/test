import click
import config


@click.command()
@click.argument("mode", default="production")
def main(mode):
    """Launches the bot."""
    mode = mode.lower()
    from core import bot

    if mode in ["dev", "development"]:
        bot.development = True

    elif mode == ["tester", "testing"]:
        bot.tester = True
    else:
        bot.production = True

    block = "#" * (len(mode) + 19)
    startmsg = f"{block}\n## Running {mode.capitalize()} Mode ## \n{block}"
    click.echo(startmsg)
    # run the application ...
    bot.run()


if __name__ == "__main__":
    main()
