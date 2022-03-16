import sys

import click
import deal
from requests.exceptions import HTTPError

import extinfo.extractors.Extractor as Extractor
from extinfo.extractors import fileinfo_com

deal.activate()

__EXTRACTORS__ = [Extractor(fileinfo_com)]


@click.command(
    no_args_is_help=True,
)
@click.version_option()
@click.argument("extension", type=str)
def cli(extension: str) -> None:
    for extractor in __EXTRACTORS__:
        try:
            result = extractor.extract(extension)
        except HTTPError as e:
            print(str(e))
        else:
            print(f"From {extractor.site}\n")
            print(
                f"# {result.description_short}\n\n",
                f"{result.description_long}\n\n",
                f"{result.how_to_open}",
            )
            sys.exit(0)

    sys.exit(1)
