class Trie(object):

    def __init__(self, word=None):
        self.word = word
        self.children = []  # list of tries

    def addChild(self, word):
        childTrie = Trie(word)
        self.children.append(childTrie)

    def insert(self, word):
        print 'Received', word
        if self.word is None:
            self.word = word  # initialise root node
        elif word == self.word:
            return  # already inserted
        elif word.startswith(self.word):  # matches current node
            remainingWord = word[len(self.word):]
            for child in self.children:
                if remainingWord.startswith(child.word):
                    child.insert(remainingWord)  # recursive insert on child
                    return  # cut search
            self.addChild(remainingWord)  # new child needed
        # else:  # insert parent node

    def __str__(self, depth=0):
        outputStr = "\t" * depth + self.word + "\n"
        for child in self.children:
            outputStr += child.__str__(depth+1)
        return outputStr


# if __name__ == '__main__':
#     def formatURL(url):
#         urlParsed = urlparse(url)
#         url = urlParsed.netloc + urlParsed.path  # only keep domain and path
#         if len(url) > 4 and url[:4] == 'www.':   # omit 'www.'
#             url = url[4:]
#         if len(url) > 0 and url[-1] == '/':      # omit trailing '/'
#             url = url[:-1]
#         return url
#
#     trie = Trie('gocardless.com')
#     trie.insert('gocardless.com/faq')
#     trie.insert('gocardless.com')
#     trie.insert('gocardless.com/faq/team')
#     trie.insert('gocardless.com/article/123')
#     print trie
