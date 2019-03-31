import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}

loadPage = lambda url: requests.get(url, headers=headers).text

# for 1.13
url = 'https://minecraft.curseforge.com/mc-mods?filter-game-version=2020709689:7132&filter-sort=4&page=%d'
page_count = 15

pages = [loadPage(url % page) for page in range(1, page_count)]


def getProjectsLinks(page):
    text = pages[page - 1]
    soup = BeautifulSoup(text, features='html.parser')

    return list(map(lambda link: "https://minecraft.curseforge.com" + link.get('href'),
                    soup.find_all('a', {'class': 'e-avatar64'})))


flatten = lambda l: [item for sublist in l for item in sublist]

projects = flatten(list(map(getProjectsLinks, range(1, page_count))))


def getSourceLink(project):
    text = loadPage(project)
    soup = BeautifulSoup(text, features='html.parser')
    return list(map(lambda e: e.get("href"),
                    list(filter(lambda e: "Source" in e.text, soup.find_all('a', {'class': 'external-link'})))))


sourceLinks = flatten(list(map(getSourceLink, projects)))

# use in finder
print(sourceLinks)
