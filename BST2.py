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
