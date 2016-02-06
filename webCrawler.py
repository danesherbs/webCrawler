from tree import URLtree
from utils import getLinksOnPage, getURL
from Queue import Queue

# Crawls a given URL and produces a sitemap
# Output is stored in current directory under 'sitemap'
def webCrawler(url):
    # TODO: only works for "https://gocardless.com"
    tree = webCrawlerDFS(url)
    sitemap = open('sitemap', 'w')
    sitemap.write(str(tree))
    sitemap.close()
    print '\n\nSitemap saved in current directory.\n\n'

def webCrawlerDFS(url):
    # initialise visited URLs
    visited = set([getURL(url)])

    # initialise queue
    queue = Queue()
    for homeLink in getLinksOnPage(url):
        queue.put(homeLink)

    # initialise tree
    tree = URLtree(url)

    while(len(visited)<10):
    # while(queue):
        link = queue.get()                        # next link
        if link not in visited:
            visited.add(link)                     # mark as seen
            map(queue.put, getLinksOnPage(link))  # visit new links later
            print link + ':',
            tree.insert(link)                     # put in tree hierarchy

    return tree


GO_CARDLESS = "https://gocardless.com"
webCrawler(GO_CARDLESS)
