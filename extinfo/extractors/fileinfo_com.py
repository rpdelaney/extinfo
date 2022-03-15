import urllib.parse

import requests
from bs4 import BeautifulSoup as bs

SITE = "fileinfo.com"
PATH = "/extension/"


def extract(extension: str) -> str:
    soup = _fetch(extension)
    return _parse(soup)


def _fetch(extension: str) -> bs:
    url = urllib.parse.urljoin(f"https://{SITE}", f"{PATH}/{extension}")
    r = requests.get(url)
    r.raise_for_status()

    soup = bs(r.text, "html.parser")

    return soup


def _parse(soup: bs) -> str:
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
    result = "\n\n".join(
        [
            f"# {header0}",
            f"{info0}\n",
            f"# {header1}",
            info1,
        ]
    )

    return result
