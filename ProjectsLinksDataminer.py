import requests
import cloudscraper
from bs4 import BeautifulSoup
import time

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

loadPage = lambda url: scraper.get(url).text

# for 1.12
url = 'https://www.curseforge.com/minecraft/mc-mods?filter-game-version=2020709689:6756&filter-sort=4&page=%d'
page_start = 1
page_count = 432

pages = [loadPage(url % page) for page in range(page_start, page_count)]


def getProjectsLinks(pageNum):
    print("parsing list page "+str(pageNum))
    text = pages[pageNum - page_start]
    soup = BeautifulSoup(text, features='html.parser')

    return list(filter(lambda e: "/mc-mods/" in e, list(map(lambda link: "https://www.curseforge.com" + str(link.get('href')),
                    soup.find_all('a', {'class': 'my-auto'})))))


flatten = lambda l: [item for sublist in l for item in sublist]

projects = flatten(list(map(getProjectsLinks, range(page_start,page_count))))


def getSourceLink(project):
    #print("parsing mod page "+project)
    time.sleep(0.1)
    text = loadPage(project)
    soup = BeautifulSoup(text, features='html.parser')
    return list(map(lambda e: e.get("href"),
                    list(filter(lambda e: "Source" in e.text, soup.find_all('a', {'class': 'text-gray-500 hover:no-underline'})))))


sourceLinks = flatten(list(map(getSourceLink, projects)))

# use in finder
# print(*sourceLinks, sep="\n")
print("source links combined!")

github_pages = open("./github-pages.txt", "w")
for e in sourceLinks:
    github_pages.write(e+"\n")
github_pages.close()


