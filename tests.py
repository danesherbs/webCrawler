###########
# UTILS.PY #
###########


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

from utils import getURL

def testGetURLreturnsNoneForInvalidURL():
    pass
