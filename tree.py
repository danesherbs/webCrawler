class Tree(object):

    def __init__(self, data=None):
        self.children = []  # list of trees
        self.data = data

    def setData(self, data):
        self.data = data
        return self

    def getData(self):
        return self.data

    def addChild(self, childData):
        childTree = Tree(childData)
        self.children.append(childTree)
        return self

    def addChildren(self, childrenData):
        for childData in childrenData:
            self.addChild(childData)
        return self

    def getChildren(self):
        return self.children


from urlparse import urlparse
class URLtree(object):

    def __init__(self, data=None):
        self.children = []  # list of URLtrees
        self.data = self.formatURL(data)

    def setData(self, data):
        self.data = data
        return self

    def getData(self):
        return self.data

    def addChild(self, childData):
        childTree = URLtree(childData)
        self.children.append(childTree)
        return self

    def addChildren(self, childrenData):
        for childData in childrenData:
            self.addChild(childData)
        return self

    def getChildren(self):
        return self.children

    # Helper for insert; omits 'http(s)://', 'www.' and trailing '/'
    def formatURL(self, url):
        urlParsed = urlparse(url)
        url = urlParsed.netloc + urlParsed.path  # only keep domain and path
        if len(url) > 4 and url[:4] == 'www.':   # omit 'www.'
            url = url[4:]
        if len(url) > 0 and url[-1] == '/':      # omit trailing '/'
            url = url[:-1]
        return url

    # PROBLEM
    #       url_given https://www.gocardless.com/blog/page27/
    #       inserted  under page27
    def insert(self, url):
        # print 'url_given', url
        url = str(self.formatURL(url))
        # print 'url_to_add', url
        path = url.split('/')
        # print 'path[0]', path[0]
        # print 'self.getData()', self.getData()
        # print 'path[0] == self.getData()', path[0] == self.getData()
        if self.getData() == path[0]:
            if len(path[1:]) > 0:  # more to add
                path = '/'.join(path[1:])
                self.insert(path)
            return self
        for child in self.getChildren():
            if child.getData() == path[0]:  # if part of explored level
                path = '/'.join(path[1:])
                child.insert(path)  # assuming not identicle string
                return self
        path = '/'.join(path)  # relative URL
        if path != '':  # don't add empty string
            self.addChild(path)
        print 'inserted', path, 'under', self.getData()
        return self

    def __str__(self):
        return self.getData()

# print urlparse('https://gocardless.com').path
# print urlparse('https://gocardless.com/blog').path

# test = 'https://gocardless.com/about/team'
# test = urlparse(test).path  # get path from URL
# test = test.split('/')
# test = filter(lambda x: x != '', test)  # ignore initial slashes
# print test

# print urlparse('gocardless.com/about/team').path.split('/')


# tree = Tree('gocardless.com')
# tree.addChild('gocardless.com/features')
# print tree.getData()
# print tree.getChildren()
# print tree.getChildren()[0]
# print tree.getChildren()[0].getData()
