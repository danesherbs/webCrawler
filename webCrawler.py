import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
import re
from collections import Counter


DOMAIN = 'gocardless.com'

# Crawls a given url and produces a sitemap
def webCrawler(url):
    webCrawlerDFS(url, [url])  # DFS on given URL

def webCrawlerDFS(url, seen):
    for subURL in getValidURLsOnPageWithinDomain(url):
        if subURL in seen:
            continue  # seen URL before
        print subURL
        seen.append(subURL)  # mark as seen
        webCrawlerDFS(subURL, seen)  # search this URL

# Joins base domain and relative link within domain to form a valid URL
def constructValidURL(url, link):
    return urljoin(url, link)

# Takes a URL and returns an exhaustive list of links present on page
def getURLsOnPage(url):
    # TODO: check for valid URL; google.com doens't work but https://www.google.com does
    rawHTML = requests.get(url).text  # extract raw HTML
    soup = BeautifulSoup(rawHTML,"lxml")  # used to parse raw HTML
    urls = []  # list of urls present on page
    for link in soup.findAll('a'):  # all anchors
        href = link.get('href')
        if href != None and len(href) > 1:  # non-empty link
            url = urljoin(url, href)  # join URLs
            urls.append(url)  # add to list
    return urls

# Uses regex from Django to determine if URL is valid (better than querying via HTTP)
def validURL(url):
    regex = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return regex.search(url) is not None

# Checks if url is within domain
def inDomain(url):
    return DOMAIN in url

# Returns all sub-URLs on given URL that are both valid and in domain
def getValidURLsOnPageWithinDomain(url):
    return filter(lambda x: inDomain(x) and validURL(x), getURLsOnPage(url))

GO_CARDLESS = "https://gocardless.com"

webCrawler(GO_CARDLESS)
# url = 'https://gocardless.com/blog/'
# print getValidURLsOnPageWithinDomain(url)
# print getURLsOnPage(url)
