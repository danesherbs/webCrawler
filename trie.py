class Trie(object):

    def __init__(self, word=''):
        self.word = word    # defaults to root node
        self.children = []  # list of tries

    def addChild(self, word):
        childTrie = Trie(word)
        self.children.append(childTrie)

    def insert(self, word):
        if word == self.word:
            return  # already inserted
        elif word.startswith(self.word):  # matches current node
            remainingWord = word[len(self.word):]
            for child in self.children:
                if remainingWord.startswith(child.word):
                    child.insert(remainingWord)  # recursive insert on child
                    return  # cut search
            self.addChild(remainingWord)  # new child needed

    def __str__(self, depth=-1):  # depth=-1 to skip needless indentation from root node ''
        outputStr = "\t" * max(depth, 0) + self.word + "\n"
        for child in self.children:
            outputStr += child.__str__(depth+1)
        return outputStr
