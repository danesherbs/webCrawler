class Tree(object):

    def __init__(self, data=None):
        self.children = []  # list of trees
        self.data = data

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def addChild(self, childData):
        childTree = Tree(childData)
        self.children.append(childTree)

    def getChildren(self):
        return self.children

tree = Tree('gocardless.com')
tree.addChild('gocardless.com/features')
print tree.getData()
print tree.getChildren()
print tree.getChildren()[0]
print tree.getChildren()[0].getData()
