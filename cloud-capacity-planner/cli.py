import logging

import click

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@click.command()
@click.option(
    "--console",
    default=True,
    is_flag=True,
    help="Output limits info to stdout/console",
    show_default=True,
)
@click.option(
    "--csv",
    "csv_",
    default=False,
    is_flag=True,
    help="Output limits to csv",
    show_default=True,
)
def cli(csv_, console):
    if console:
        print("Hello World")


if __name__ == "__main__":
    cli()
