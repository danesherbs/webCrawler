import requests
import BeautifulSoup as soup

def webCrawler(url):
    '''
    Crawls a given url and produces a sitemap
    '''

    # TODO: check for valid URL; google.com doens't work but https://www.google.com does

    sourceCode = requests.get(url)

    print sourceCode.json()

# webCrawler("https://gocardless.com/")
webCrawler("https://google.com/")
