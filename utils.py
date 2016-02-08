from urllib2 import urlopen, HTTPError, URLError
from urlparse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests


cache = {}  # proxy cache (stores queried URLs)

# Takes a URL and returns an exhaustive list of links present on page
def getLinksOnPage(url):
    rawHTML = requests.get(url).text  # extract raw HTML
    soup = BeautifulSoup(rawHTML)     # used to parse raw HTML
    links = []
    for anchor in soup.findAll('a'):
        href = anchor.get('href')
        absURL = urljoin(url, href)  # absolute URL
        absURL = getURL(absURL)      # see if invalid or redirected
        if absURL is not None:       # if genuine URL
            links.append(absURL)     # add URL to list
    return links

# Retrieves URL (if redirected, retrieves redirected URL)
# Uses proxy cache in case connection is slow
def getURL(url):
    if containsQueries(url) or containsFragments(url):
        cache[url] = None
    elif url not in cache:
        try:
            cache[url] = urlopen(url).geturl()
        except (HTTPError, URLError):
            # HTTPError - dead link
            # URLError  - invalid URL (e.g. mailto)
            cache[url] = None
    return cache[url]

# Checks if queries in URL
def containsQueries(url):
    return urlparse(url).query != ''

# Checks if fragments in URL
def containsFragments(url):
    return urlparse(url).fragment != ''
