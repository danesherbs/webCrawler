############
# UTILS.PY #
############


# containsQueries

from utils import containsQueries

def testContainsQueriesReturnsTrueForStringWithQuery():
    queryStr = 'https://gocardless.com/contact-sales/?s=pricing'
    assert containsQueries(queryStr)

def testContainsQueriesReturnsFalseForStringWithoutQuery():
    queryStr = 'https://gocardless.com/contact-sales/'
    assert not containsQueries(queryStr)


# containsFragments

from utils import containsFragments

def testContainsFragmentsReturnsTrueForStringWithFragment():
    fragmentStr = 'https://gocardless.com/#learn-more'
    assert containsFragments(fragmentStr)

def testContainsFragmentsReturnsFalseForStringWithoutFragment():
    fragmentStr = 'https://gocardless.com/pricing/'
    assert not containsFragments(fragmentStr)


# getURL
# Better implementation if more time available: use a mock of the
# remote service to avoid queries potentially slowing down tests

from utils import getURL, getLinksOnPage
import os

def testGetURLreturnsNoneForSyntaticallyIncorrectURL():
    url = getURL('not_a_url')
    assert url is None

def testGetURLreturnsNoneForNonExistantWebsite():
    url = getURL('https://useacard.com')
    assert url is None

def testGetURLreturnsNoneForURLnotPointingToPage():
    url = getURL('mailto:someone@example.com')
    assert url is None

def testGetURLreturnsValidURLforValidURL():
    GO_CARDLESS = 'https://gocardless.com'
    url = getURL(GO_CARDLESS)
    assert url == GO_CARDLESS

def testGetLinksOnPage():
    # Test is fragile - assumes number of links on page won't change
    # With more time: create a mock website with known number of links
    # and don't change it.
    GOOGLE = 'https://gocardless.com'
    links = getLinksOnPage(GOOGLE)
    assert len(links) == 53



###########
# TRIE.PY #
###########


from trie import Trie

def testTrieOutput():

    trie = Trie()
    trie.insert('gocardless.com')
    trie.insert('gocardless.com/faq')
    trie.insert('gocardless.com')
    trie.insert('gocardless.com/faq/team')
    trie.insert('gocardless.com/article/123')
    trie.insert('gocardless.com/article/123/123')

    expectedOutput = open('testTrie','r')
    assert str(trie) == expectedOutput.read()
    expectedOutput.close()
