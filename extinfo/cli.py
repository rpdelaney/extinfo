import sys
from typing import NoReturn

import click
import deal
from rich.console import Console

from extinfo.extractors import fileinfo_com, filesuffix_com

from .exceptions import ExtensionNotFoundError
from .utils import Extractor

deal.activate()

__EXTRACTORS__ = (
    Extractor(filesuffix_com),
    Extractor(fileinfo_com),
)


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
def cli(extension: str, short: bool, one: bool) -> NoReturn:
    console = Console()
    results = []
    for extractor in __EXTRACTORS__:
        try:
            results.append(extractor.extract(extension))
        except ExtensionNotFoundError as e:
            console.log(str(e))

    # flatten and listify
    reports = [report for sublist in results for report in sublist]

    for report in reports:
        if short:
            console.print(f"{report.description_short}")
        else:
            console.print(f"# {report.description_short}")
            console.print("")
            if report.description_long:
                console.print(f"{report.description_long}")
                console.print("")
            if report.how_to_open:
                console.print("## How to open")
                console.print("")
                console.print(report.how_to_open)
                console.print("")
        if one:
            break
    else:
        sys.exit(1)

    sys.exit(0)
