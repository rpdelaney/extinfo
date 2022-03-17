import string

from ..utils import Report, fetch

SITE = "filesuffix.com"
PATH = "/en/extension"


def extract(extension: str) -> Report:
    soup = fetch(site=SITE, path=PATH, extension=extension)
    result = result = soup.find(name="div", attrs={"id": "result"}).findChild(
        attrs={"class": ["exttab"]}
    )

    description_short = "".join(
        c
        for c in result.findChild(
            name="h2",
            attrs={"id": "ext0"},
        ).text.strip()
        if c in string.ascii_letters + " "
    ).strip()
    description_long = result.findChild(
        name="div",
        attrs={"class": ["el"]},
    ).text.strip()
    how_to_open = (
        result.findChild(
            name="a",
            attrs={"class": ["sl"]},
        )
        .get("title")
        .strip()
    )

    return Report(
        description_short=description_short,
        description_long=description_long,
        how_to_open=how_to_open,
    )
