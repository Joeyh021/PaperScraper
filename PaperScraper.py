from bs4 import BeautifulSoup
import requests as rq
from os import makedirs


# edit these two parameters
COOKIE_TOKEN = ""

s = rq.Session()
s.cookies["WarwickSSO"] = COOKIE_TOKEN


def downloadpdf(url: str, dep: str):

    file = s.get(url)
    filename: str = url.split('/')[-1]
    year: str = url.split('/')[-2]

    makedirs(f"papers/{dep}/{year}", exist_ok=True)

    with open(f"papers/{dep}/{year}/{filename}", "wb+") as f:
        f.write(file.content)


def getDepartment(dep: list[str]):
    URL=f"https://warwick.ac.uk/services/exampapers/?q=&department={dep[0]}&year="
    page = s.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')

    for tag in soup.find_all("a"):
        url: str = tag.get("href")
        if url.endswith(".pdf"):
            print(url)
            downloadpdf(url,dep[1])

def chosenDepartments():
    departments=[]
    with open("departments.txt") as dep:
        for line in dep.readlines():
            if line[0]!="#":
                parts=line.strip().split(" ")
                departments.append([parts[0]," ".join(parts[1:])])
    return departments

for department in chosenDepartments():
    getDepartment(department)