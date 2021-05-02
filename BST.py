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
            self.setRoot(node) #print 'No root for Tree, Adding Root: ' + node.value
        else:
            if(node.value <= root.value):
                if (root.left == None):#print 'Node value ' + node.value + ' <= ' + root.value + ' checking left tree'
                    root.left = node #print 'Left Tree without root, adding root: ' + node.value
                else:
                    self.addNode(root.left,node) #print 'Root exists, adding Node: ' + node.value + ' to root: ' + root.left.value
            else:
                if(root.right == None): #print 'Node value ' + node.value + ' > ' + root.value + ' checking right tree'
                    root.right = node #print 'Right Tree without root, adding root: ' + node.value
                else:
                    self.addNode(root.right,node) #print 'Root exists, adding Node: ' + node.value + ' to root: ' + root.right.values
