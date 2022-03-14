import sys

import click
import deal

deal.activate()


@click.command(
    no_args_is_help=True,
)
@click.version_option()
def cli() -> int:
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(cli())
