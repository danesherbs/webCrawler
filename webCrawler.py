import requests
from bs4 import BeautifulSoup
from urlparse import urljoin, urlparse
import re
from collections import Counter


DOMAIN = 'gocardless.com'

# Crawls a given url and produces a sitemap
def webCrawler(url):
    seen = [URLid(url)]
    webCrawlerDFS(url, seen)  # DFS on given URL
    seen = sorted(seen)
    for seenURL in seen:
        depth = Counter(seenURL)['/']
        print depth * '\t' + seenURL

def webCrawlerDFS(url, seen):
    if len(seen) > 100:
        return seen
    for subURL in generateSubURLs(url):
        subURLid = URLid(subURL)
        if subURLid in seen:
            continue  # seen URL before
        print subURLid
        seen.append(subURLid)  # mark as seen
        webCrawlerDFS(subURL, seen)  # search this URL

def URLid(url):
    # TODO: fix - it includes www.gocardless.com and gocardless.com
    url = url.split('/')[2:]
    url = filter(lambda x: x!='', url)
    return '/'.join(url)

# Takes a URL and returns an exhaustive list of links present on page
def getURLsOnPage(url):
    # TODO: check for valid URL; google.com doens't work but https://www.google.com does
    rawHTML = requests.get(url).text  # extract raw HTML
    soup = BeautifulSoup(rawHTML)  # used to parse raw HTML
    urls = []  # list of urls present on page
    for link in soup.findAll('a'):  # all anchors
        href = link.get('href')
        if href != None and len(href) > 1:  # non-empty link
            url = urljoin(url, href)  # join URLs
            urls.append(url)  # add to list
    return urls

# Uses regex from Django to determine if URL is valid (better than querying via HTTP)
def validURL(url):
    parsedURL = urlparse(url)
    if parsedURL.query != '' or parsedURL.fragment != '':
        return False  # no queries or fragments permitted
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
def generateSubURLs(url):
    return filter(lambda x: inDomain(x) and validURL(x), getURLsOnPage(url))

GO_CARDLESS = "https://gocardless.com"
webCrawler('https://blog.gocardless.com')





##############################################
