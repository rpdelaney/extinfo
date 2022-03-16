import urllib.parse
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup as bs


@dataclass
class Report:
    description_short: str
    description_long: str
    how_to_open: str


def fetch(*, site: str, path: str, extension: str) -> bs:
    url = urllib.parse.urljoin(f"https://{site}", f"{path}/{extension}")
    r = requests.get(url)
    r.raise_for_status()

    soup = bs(r.text, "html.parser")

    return soup
