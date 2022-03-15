import sys

import click
import deal
from requests.exceptions import HTTPError

from extinfo.extractors import fileinfo_com

deal.activate()

__EXTRACTORS__ = [fileinfo_com]


@click.command(
    no_args_is_help=True,
)
@click.version_option()
@click.argument("extension", type=str)
def cli(extension: str) -> int:
    for extractor in __EXTRACTORS__:
        try:
            result = extractor.extract(extension)
        except HTTPError as e:
            print(str(e))
        else:
            print(f"From {extractor.SITE}\n")
            print(
                f"# {result.description_short}\n\n",
                f"{result.description_long}",
            )

    return 0


if __name__ == "__main__":
    sys.exit(cli())
