import requests
from bs4 import BeautifulSoup as bs


def _fetch(extension: str) -> str:
    url = f"https://fileinfo.com/extension/{extension}"
    r = requests.get(url)
    r.raise_for_status()

    soup = bs(r.text, "html.parser")
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
            f"From {url}",
            f"# {header0}",
            f"{info0}\n",
            f"# {header1}",
            info1,
        ]
    )

    return result
