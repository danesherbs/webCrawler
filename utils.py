from urllib2 import urlopen, HTTPError, URLError
import re
from urlparse import urljoin, urlparse, urlsplit
import requests
from bs4 import BeautifulSoup



DOMAIN = 'gocardless.com'
cache = {}  # queried URLs



# Regex from Djano
def correctSyntax(url):
    regex = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return regex is not None

def noQueries(url):
    return urlparse(url).query == ''

def noFragments(url):
    return urlparse(url).fragment == ''

# Checks if url is within domain
def inDomain(url):
    return DOMAIN in urlparse(url).netloc

def validURL(url):
    return correctSyntax(url) and inDomain(url) and noFragments(url) and noQueries(url)

def getURL(url):
    # TODO: slow connection - just check if valid
    try:
        if not validURL(url):
            cache[url] = None
        elif url not in cache:
            cache[url] = urlopen(url).geturl()
    except (HTTPError, URLError):
        # HTTPError - dead link
        # URLError  - invalid URL (e.g. mailto)
        cache[url] = None
    return cache[url]

# Takes a URL and returns an exhaustive list of links present on page
def getLinksOnPage(url):
    rawHTML = requests.get(url).text  # extract raw HTML
    soup = BeautifulSoup(rawHTML)     # used to parse raw HTML
    links = []
    for anchor in soup.findAll('a'):
        href = anchor.get('href')
        absURL = urljoin(url, href)   # absolute URL
        absURL = getURL(absURL)       # see if invalid or redirected
        if absURL is not None:        # if genuine URL
            links.append(absURL)      # add URL to list
    return links



def printTree(root):
    visited, stack = set(), [root]
    while stack:
        subTree = stack.pop()  # next tree
        if subTree not in visited:
            visited.add(subTree)
            stack.extend(subTree.getChildren())
    return visited

# print formatURL("https://gocardless.com")
# print formatURL("https://gocardless.com/")
# print formatURL("http://gocardless.com")
# print formatURL("http://gocardless.com/")
# print formatURL("http://gocardless.com/about/")
# print formatURL("https://gocardless.com/about")
# print formatURL("https://www.gocardless.com/about")
# print formatURL("https://www.gocardless.com/about")
