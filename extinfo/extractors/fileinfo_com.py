import re

from ..utils import Report, fetch

SITE = "fileinfo.com"
PATH = "/extension/"


def extract(extension: str) -> Report:
    soup = fetch(site=SITE, path=PATH, extension=extension)
    description_short = soup.find_all("h2")[0].text.strip()

    infoboxes = soup.find_all(attrs={"class": "infoBox"})
    description_long = infoboxes[0].text.strip()
    how_to_open = re.sub(r"\n+", "\n\n", infoboxes[1].text).strip()

    report = Report(
        description_short=description_short,
        description_long=description_long,
        how_to_open=how_to_open,
    )
    return report
