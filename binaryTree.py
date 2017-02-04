class Node:
    left, right, value = None, None, 0
    def __init__(self,val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def setRoot(self,node):
        self.root = node

    def addNode(self,root,node):
        if(root == None):
            #print 'No root for Tree, Adding Root: ' + node.value
            self.setRoot(node)
        else:
            if(node.value <= root.value):
                #print 'Node value ' + node.value + ' <= ' + root.value + ' checking left tree'
                if (root.left == None):
                    #print 'Left Tree without root, adding root: ' + node.value
                    root.left = node
                else:
                    #print 'Root exists, adding Node: ' + node.value + ' to root: ' + root.left.value
                    self.addNode(root.left,node)
            else:
                #print 'Node value ' + node.value + ' > ' + root.value + ' checking right tree'
                if(root.right == None):
                    #print 'Right Tree without root, adding root: ' + node.value
                    root.right = node
                else:
                    self.addNode(root.right,node)
                    #print 'Root exists, adding Node: ' + node.value + ' to root: ' + root.right.values



def fillTree(t):
    #print 'Filling Tree With Values'
    values = ['P','F','S','B','H','R','W','A','M']
    #values = ['F','B','G','A','D','I','C','E','H']
    #values = ['P','F']
    for item in values:
        n = Node(item)
        if t.root == None:
            t.root = n
        else:
            t.addNode(t.root,n)
        #print 'Tree Root: ' + t.root.value

def preOrder(root):
    if(root != None):
        print root.value,
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print root.value,
        inOrder(root.right)

def postOrder(root):
    if(root != None):
        postOrder(root.left)
        postOrder(root.right)
        print root.value,

t = Tree()
print "Filling Tree"
fillTree(t)
print "Pre-Order"
preOrder(t.root)
print "\nIn-Order"
inOrder(t.root)
print "\nPost-Order"
postOrder(t.root)
