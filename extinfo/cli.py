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
@click.option(
    "--short/--long",
    help="Print only short descriptions",
    default=False,
)
@click.option(
    "-1",
    "--one/--all",
    help="Print print only one report, from the first extractor",
    default=False,
)
@click.argument("extension", type=str)
def cli(extension: str, short: bool, one: bool) -> None:
    for extractor in __EXTRACTORS__:
        try:
            results = extractor.extract(extension)
        except ExtensionNotFoundError as e:
            print(str(e), file=sys.stderr)
        else:
            for report in results:
                if short:
                    print(f"{report.description_short}")
                else:
                    print(f"# From {extractor.site}\n")
                    print(f"## {report.description_short}")
                    print("")
                    if report.description_long:
                        print(f"{report.description_long}")
                        print("")
                    if report.how_to_open:
                        print("### How to open")
                        print("")
                        print(report.how_to_open)
                        print("")
            if one:
                return

    sys.exit(1)
