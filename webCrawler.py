from tree import URLtree
from utils import getLinksOnPage, getURL

# Crawls a given url and produces a sitemap
def webCrawler(url):
    tree = webCrawlerDFS(url)
    # print tree
    # for seenURL in visited:
    #     depth = Counter(seenURL)['/']
    #     print depth * '\t' + seenURL

def webCrawlerDFS(url):
    # initialise visited nodes
    visited = set([getURL(url)])

    # initialise stack
    homepageLinks = getLinksOnPage(url)
    stack = homepageLinks

    # initialise tree
    # tree = URLtree(url).addChildren(homepageLinks)
    tree = URLtree(url)

    # while(len(visited)<20):
    while(stack):
        link = stack.pop()  # next link
        if link not in visited:
            # print link
            visited.add(link)                   # mark as seen
            stack.extend(getLinksOnPage(link))  # visit new links later
            # print 'link', link, type(link)
            tree.insert(link)                   # add link hierarchy

    return tree


GO_CARDLESS = "https://gocardless.com"
webCrawler(GO_CARDLESS)


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
