import urllib.parse
from dataclasses import dataclass
from types import ModuleType

import requests
from bs4 import BeautifulSoup as bs

from .exceptions import ExtensionNotFoundError, ClientForbiddenError


@dataclass()
class Report:
    description_short: str
    description_long: str
    how_to_open: str

    def __post_init__(self) -> None:
        self.short_form = self.description_short
        self.long_form = (
            self.description_short
            + "\n"
            + self.description_long
            + "\n"
            + self.how_to_open
        )


def fetch(*, site: str, path: str, extension: str) -> bs:
    url = urllib.parse.urljoin(f"https://{site}", f"{path}/{extension}")

    r = requests.get(url)

    match r.status_code:
        case 404:
            raise ExtensionNotFoundError(f"404 from site for url: {url}")
        case 403:
            raise ClientForbiddenError(f"403 from site for url: {url}")
        case 200:
            return bs(r.text, "html.parser")
        case _:
            r.raise_for_status()


class Extractor:
    def __init__(self, extractor_module: ModuleType) -> None:
        self.extract = extractor_module.extract
        self.site = extractor_module.SITE
