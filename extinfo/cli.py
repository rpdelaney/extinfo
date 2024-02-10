import sys
from typing import NoReturn

import click
import deal
from rich.console import Console

from extinfo.extractors import fileinfo_com, filesuffix_com

from .exceptions import ExtinfoError
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
        except ExtinfoError as e:
            console.log(str(e))

    # flatten and listify
    reports = [report for sublist in results for report in sublist]

    for report in reports:
        if short:
            console.print(report.short_form)
        else:
            console.print(report.long_form, "\n\n")
        if one:
            break
    else:
        sys.exit(1)

    sys.exit(0)
