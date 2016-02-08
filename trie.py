class Trie(object):

    def __init__(self, data):
        self.data = data
        self.children = []  # list of tries

    def getData(self):
        return self.data

    def getChildren(self):
        return self.children

    def addChild(self, data):
        childTrie = Trie(data)
        self.children.append(childTrie)

    def insert(self, word):
        if word == '':
            return  # nothing to insert
        elif word.startswith(self.data):  # matches current node
            for child in self.children:
                if child.data == word[len(self.data):]:
                    child.insert(word[len(self.data):])  # recursive insert on child
                    return  # cut search
            self.addChild(word[len(self.data):])  # new child needed
        else:  # new child needed
            self.addChild(word)
            # newChild.insert(word[1:])

    # def insert(self, word):
    #     if word == '':  # nothing to insert
    #         return
    #     elif self.getData() == word[0]:  # matches current node
    #         self.insert(word[1:])
    #     else:  # in existing child or new child needed
    #         for child in self.getChildren():
    #             if child.getData() == word[0]:  # matches existing child
    #                 child.insert(word[1:])
    #                 return  # cut search after insertion in existing child
    #         newChild = Trie(word[0])  # new child needed
    #         self.addChild(newChild)
    #         newChild.insert(word[1:])

    def __str__(self, depth=0):
        outputStr = "  " * depth + str(self.getData()) + "\n"
        for child in self.getChildren():
            outputStr += child.__str__(depth+1)
        return outputStr


from urlparse import urlparse
class URLtrie(Trie):

    def __init__(self, data):
        self.children = []  # list of URLtries
        self.data = self.formatURL(data)

    def addChild(self, childData):
        childTrie = URLtrie(childData)  # add URLtrie instead of Trie
        self.children.append(childTrie)
        return self

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
            if len(path[1:]) > 0:           # more to add
                path = '/'.join(path[1:])
                self.insert(path)
            return self
        for child in self.getChildren():
            if child.getData() == path[0]:  # if part of explored level
                path = '/'.join(path[1:])
                child.insert(path)          # assuming not identicle string
                return self
        path = '/'.join(path)               # relative URL
        if path != '':                      # don't add empty string
            self.addChild(path)
            print 'inserted', path, 'under', self.getData()
        return self



if __name__ == '__main__':
    trie = Trie('d')
    print trie
    trie.insert('dog')
    print trie
    trie.insert('doggie')
    print trie

    # trie = Trie('g')
    # print trie
    # trie.insert('gg')
    # print trie
    # trie.insert('ggg')
    # print trie
