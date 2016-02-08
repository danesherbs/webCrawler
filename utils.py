from urllib2 import urlopen, HTTPError, URLError
from urlparse import urljoin, urlparse, urlsplit
from bs4 import BeautifulSoup
import requests
import re


DOMAIN = 'gocardless.com'
cache = {}  # queried URLs

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

# Retrieves URL (if redirected, retrieves redirected URL)
# Uses proxy cache in case connection is slow
def getURL(url):
    # TODO: slow connection - just check if valid
    if not validURL(url):
        cache[url] = None
    elif url not in cache:
        try:
            cache[url] = urlopen(url).geturl()
        except (HTTPError, URLError):
            # HTTPError - dead link
            # URLError  - invalid URL (e.g. mailto)
            cache[url] = None
    return cache[url]

# Combines multiple checks in one
def validURL(url):
    return correctSyntax(url) and inDomain(url) and noFragments(url) and noQueries(url)

# Checks syntax of URL
# Regex from Django
def correctSyntax(url):
    regex = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return regex is not None

# Checks if no queries in URL
def noQueries(url):
    return urlparse(url).query == ''

# Checks if no fragments in URL
def noFragments(url):
    return urlparse(url).fragment == ''

# Checks if URL is within domain
def inDomain(url):
    return DOMAIN in urlparse(url).netloc
