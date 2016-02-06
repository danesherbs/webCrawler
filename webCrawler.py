from tree import URLtree
from utils import getLinksOnPage, getURL
from Queue import Queue

class WebCrawler(object):

    # Crawls given URL and produces sitemap (stored in current directory)
    def crawl(self, url):
        tree = self.webCrawlerBFS(url)
        sitemap = open('sitemap', 'w')
        sitemap.write(str(tree))
        sitemap.close()
        print '\n\nSitemap saved in current directory.\n\n'

    # Helper for crawl -- constructs trie via breadth first search
    def webCrawlerBFS(self, url, limit=100):
        # initialise visited URLs
        visited = set([getURL(url)])
        # initialise queue
        queue = Queue()
        for homeLink in getLinksOnPage(url):
            queue.put(homeLink)
        # initialise tree
        tree = URLtree(url)
        while(len(visited) < limit):
            link = queue.get()                        # next link
            if link not in visited:
                visited.add(link)                     # mark as seen
                map(queue.put, getLinksOnPage(link))  # visit new links later
                print link + ':',
                tree.insert(link)                     # put in tree hierarchy
        return tree

if __name__ == '__main__':
    GO_CARDLESS = "https://gocardless.com"
    webCrawler = WebCrawler()
    webCrawler.crawl(GO_CARDLESS)
