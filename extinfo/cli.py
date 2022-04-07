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
    print(f"# {extension}\n")
    for extractor in __EXTRACTORS__:
        try:
            results = extractor.extract(extension)
        except ExtensionNotFoundError as e:
            print(str(e))
        else:
            print(f"## From {extractor.site}\n")
            for report in results:
                print(f"### {report.description_short}")
                print("")
                if report.description_long:
                    print(f"{report.description_long}")
                    print("")
                if report.how_to_open:
                    print("#### How to open")
                    print("")
                    print(report.how_to_open)
                    print("")

    sys.exit(1)
