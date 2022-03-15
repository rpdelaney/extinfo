import urllib.parse

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
    # TODO: make this not horrific and awful
    #
    headers = soup.find_all("h2")
    header0 = headers[0].text.strip()
    header1 = headers[1].text.strip()

    infoboxes = soup.find_all(attrs={"class": "infoBox"})
    info0 = infoboxes[0].text.strip()
    info1 = (
        infoboxes[1].text.strip().replace("\n\n\n", "\n").replace("\n", "\n\n")
    )
    report = Report(
        description_short=header0,
        description_long=info0,
        how_to_open=info1,
    )
    return report
