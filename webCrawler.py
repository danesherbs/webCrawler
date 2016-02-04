import requests
from bs4 import BeautifulSoup
import Queue
import defaultdict

def webCrawler(url):
    '''
    Crawls a given url and produces a sitemap

    Strategy:
        - BFS search (add all unseen pages to queue)
            - Only add links with host gocardless
    '''

    # TODO: check for valid URL; google.com doens't work but https://www.google.com does


    # Needed for BFS:
    unvisited = Queue.Queue(str)  # queue of unvisited links
    seen = defaultdict(bool)      # dictionary of seen links

    # initialise queue and dictionary
    links = getLinksOnPage(url)  # store links on given URL in list
    addListToQueue(unvisited, links)  # initialise queue
    addListToDictionary(seen, links)  # mark as each seen


    while (not unvisited.empty()):
        print unvisited.get()


def addListToDictionary(dictionary, links):  # TODO: think of a better name
    '''
    Adds elements of list to dictionary
    '''
    map(lambda link: dictionary[link]=True, links)

def addListToQueue(queue, links):
    '''
    Adds elements of list to queue
    '''
    map(queue.put, links)


def getLinksOnPage(url):
    '''
    Input:  URL
    Output: Exhaustive list of links present on page
    '''
    html = requests.get(url).text  # extract raw HTML
    soup = BeautifulSoup(html,"lxml")
    links = []
    for link in soup.findAll('a', href=True):  # all anchors with href
        href = link.get('href')
        if href != None and len(href) > 1:  # valid link
            links.append(href)
    return links


# webCrawler("https://gocardless.com/")
# webCrawler("https://google.com/")

GO_CARDLESS = "https://gocardless.com/"

webCrawler(GO_CARDLESS)

# getLinksOnPage(GO_CARDLESS)
# getLinksOnPage("http://tools.com/")
