from bs4 import BeautifulSoup
import requests as rq
from os import makedirs


# edit these two parameters
URL = "https://warwick.ac.uk/services/exampapers/?q=&department=ES&year="
COOKIE_TOKEN = "your token here"


s = rq.Session()
s.cookies["WarwickSSO"] = COOKIE_TOKEN


def downloadpdf(url: str):

    file = s.get(url)
    filename: str = url.split('/')[-1]
    year: str = url.split('/')[-2]

    makedirs(f"papers/{year}", exist_ok=True)

    with open(f"papers/{year}/{filename}", "wb+") as f:
        f.write(file.content)


page = s.get(URL).text
soup = BeautifulSoup(page, 'html.parser')

for tag in soup.find_all("a"):
    url: str = tag.get("href")
    if url.endswith(".pdf"):
        print(url)
        downloadpdf(url)
