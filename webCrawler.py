from trie import Trie
from utils import getLinksOnPage, getURL
from collections import deque
from urlparse import urlparse


class WebCrawler(object):

    # Uses trie (produced by crawl) to write a sitemap in current directory.
    def generateSitemap(self, domain, limit=100):
        trie = self.crawl(domain, limit)
        sitemap = open('sitemap', 'w')
        sitemap.write(str(trie))
        sitemap.close()
        print '\n\nSitemap saved in current directory.\n\n'

    # BFS through given domain; produces a trie storing the hierarchy.
    def crawl(self, domain, limit=100):
        visited = set()                    # initialise visited URLs
        queue   = deque([getURL(domain)])  # initialise queue
        trie    = Trie()                   # initialise trie
        while(queue and len(visited) < limit):
            link = queue.popleft()                  # next link
            if link not in visited and self.inDomain(link, domain):
                visited.add(link)                   # mark as seen
                queue.extend(getLinksOnPage(link))  # visit new links later
                trie.insert(self.formatURL(link))   # put in trie hierarchy
        return trie

    # Helper for crawl; omits 'http(s)://', 'www.' and trailing '/'
    # Used to avoid trie storing duplicates (eg 'www.abc.com' and 'abc.com').
    def formatURL(self, url):
        parsedURL = urlparse(url)
        url = parsedURL.netloc + parsedURL.path  # take domain and path
        if len(url) > 4 and url[:4] == 'www.':   # omit 'www.'
            url = url[4:]
        if len(url) > 0 and url[-1] == '/':      # omit trailing '/'
            url = url[:-1]
        return url

    # Test if link is within given domain
    def inDomain(self, link, domain):
        return self.formatURL(domain) in urlparse(link).netloc


if __name__ == '__main__':
    GO_CARDLESS = "https://gocardless.com"
    webCrawler = WebCrawler()
    webCrawler.generateSitemap(GO_CARDLESS, limit=30)
