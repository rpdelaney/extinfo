import urllib.parse
import re

import requests
from bs4 import BeautifulSoup as bs

from ..utils import Report

SITE = "fileinfo.com"
PATH = "/extension/"


def extract(extension: str) -> Report:
    soup = _fetch(extension)
    return _parse(soup)


def _fetch(extension: str) -> bs:
    url = urllib.parse.urljoin(f"https://{SITE}", f"{PATH}/{extension}")
    r = requests.get(url)
    r.raise_for_status()

    soup = bs(r.text, "html.parser")

    return soup


def _parse(soup: bs) -> Report:
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
