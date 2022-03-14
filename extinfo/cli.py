import sys

import click
import deal

from .scraper import _fetch

deal.activate()


@click.command(
    no_args_is_help=True,
)
@click.version_option()
@click.argument("extension", type=str)
def cli(extension: str) -> int:
    result = _fetch(extension)
    print(result)

    return 0


if __name__ == "__main__":
    sys.exit(cli())
