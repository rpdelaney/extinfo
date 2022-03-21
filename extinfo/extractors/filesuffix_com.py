import string

from bs4 import BeautifulSoup as bs

from ..utils import Report, fetch

SITE = "filesuffix.com"
PATH = "/en/extension"


def _parse_result(soup: bs) -> Report:
    description_short = "".join(
        c
        for c in soup.findChild(name="h2").text
        if c in string.ascii_letters + " "
    ).strip()

    description_long = soup.findChild(
        name="div",
        attrs={"class": ["el"]},
    ).text.strip()
    prefix = "Description:"
    if description_long.startswith(prefix):
        description_long = description_long[len(prefix) :]  # noqa: E203

    how_to_open = (
        (
            soup.findChild(
                name="a",
                attrs={"class": ["sl"]},
            )
            or {}
        )
        .get("title", "")
        .strip()
    )

    return Report(
        description_short=description_short,
        description_long=description_long,
        how_to_open=how_to_open,
    )


def extract(extension: str) -> list[Report]:
    soup = fetch(site=SITE, path=PATH, extension=extension)
    exttabs = soup.find_all(name="div", class_="exttab")

    return [_parse_result(exttab) for exttab in exttabs]
