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

    def __str__(self, depth=0):
        outputStr = "\t" * depth + str(self.getData()) + "\n"
        for child in self.getChildren():
            outputStr += child.__str__(depth+1)
        return outputStr


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

    def insert(self, url):
        url = str(self.formatURL(url))
        path = url.split('/')
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
