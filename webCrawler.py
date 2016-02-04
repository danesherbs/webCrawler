import requests
from bs4 import BeautifulSoup
import Queue
from collections import defaultdict
from urlparse import urljoin
import re

DOMAIN = 'gocardless.com'

# Crawls a given url and produces a sitemap
def webCrawler(url):
    # TODO: Only add links with host gocardless
    # Use BFS to make it balanced. DFS would be easier but less readable.

    # Needed for BFS
    unvisited = Queue.Queue(str)  # queue of unvisited links
    seen = defaultdict(bool)      # dictionary of seen links
    seen[url] = True  # seen main page

    # Start BFS on given URL
    webCrawlerBFS(url, unvisited, seen)

    # drawSitemap(seen.keys())

    return None  # print a hierarchical tree structure?

def webCrawlerBFS(url, unvisited, seen):
    for subURL in getValidURLsOnPageWithinDomain(url):
        print 'subURL', subURL
        if not seen[subURL]:  # found a URL we haven't seen before!
            seen[subURL] = True
            unvisited.put(subURL)  # visit it later
    if not unvisited.empty():
        webCrawlerBFS(unvisited.get(), unvisited, seen)  # search next URL in queue

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
            url = urljoin(url, href)  # construct URL
            urls.append(href)  # seen another URL!
    return urls

# Uses regex from Django to determine if URL is valid
def validURL(url):
    regex = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return regex.search(url) is not None

# DOMAIN is in url
def inDomain(url):
    return DOMAIN in url

# Returns all sub-URLs on given URL that are both valid and in domain
def getValidURLsOnPageWithinDomain(url):
    return filter(lambda x: inDomain(x) and validURL(x), getURLsOnPage(url))

GO_CARDLESS = "https://gocardless.com"

webCrawler(GO_CARDLESS)
# print getURLsOnPage(GO_CARDLESS)
