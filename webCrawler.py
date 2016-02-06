from tree import URLtree
from utils import getLinksOnPage, getURL
from Queue import Queue

# Crawls a given url and produces a sitemap
def webCrawler(url):
    tree = webCrawlerDFS(url)
    # print tree

def webCrawlerDFS(url):
    # initialise visited nodes
    visited = set([getURL(url)])

    # initialise queue
    queue = Queue()
    for homeLink in getLinksOnPage(url):
        queue.put(homeLink)

    # initialise tree
    tree = URLtree(url)

    # while(len(visited)<20):
    while(queue):
        link = queue.get()  # next link
        if link not in visited:
            visited.add(link)                     # mark as seen
            map(queue.put, getLinksOnPage(link))  # visit new links later
            print 'url_given', link
            tree.insert(link)                     # add link hierarchy

    return tree


GO_CARDLESS = "https://gocardless.com"
webCrawler(GO_CARDLESS)

# homepageLinks = getLinksOnPage(GO_CARDLESS)
# queue = Queue()
# for homepageLink in homepageLinks:
#     queue.put(homepageLink)
# queue.put('asdasdas')
# print queue.get()

# print correctSyntax('mailto:help@gocardless.com')
# print validURL('mailto:help@gocardless.com')
# print validURL('')

# print formatURL("https://gocardless.com")
# print formatURL("https://gocardless.com/")
# print formatURL("http://gocardless.com")
# print formatURL("http://gocardless.com/")
# print formatURL("http://gocardless.com/about/")
# print formatURL("https://gocardless.com/about")

# frag = 'https://gocardless.com/#learn-more'
# print urlopen(frag).geturl()

# print urlsplit(GO_CARDLESS).geturl()
# print urlsplit("https://blog.gocardless.com").geturl()
# print urlsplit("https://gocardless.com/blog").geturl()




##############################################
