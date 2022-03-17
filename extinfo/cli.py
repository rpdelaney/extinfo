import sys

import click
import deal

from extinfo.extractors import fileinfo_com, filesuffix_com

from .exceptions import ExtensionNotFoundError
from .utils import Extractor

deal.activate()

__EXTRACTORS__ = [
    Extractor(filesuffix_com),
    Extractor(fileinfo_com),
]


@click.command(
    no_args_is_help=True,
)
@click.version_option()
@click.argument("extension", type=str)
def cli(extension: str) -> None:
    for extractor in __EXTRACTORS__:
        try:
            result = extractor.extract(extension)
        except ExtensionNotFoundError as e:
            print(str(e))
        else:
            print(f"From {extractor.site}\n")
            print(
                f"# {result.description_short}\n\n",
                f"{result.description_long}\n\n",
                "# How to open\n\n",
                f"{result.how_to_open}",
            )
            sys.exit(0)

    sys.exit(1)
