


#---------------STRUCTURE OF BINARY TREE--------------#

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right= None

class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)


#------------DISPLAY METHOD OF BINARY TREE------------#

    def print_preodrer(self,start):
        if (start is not None) :
            print(start.value)
            self.print_preodrer(start.left)
            self.print_preodrer(start.right)

    def print_intodrer(self,start):
        if (start is not None) :
            self.print_intodrer(start.left)
            print(start.value)
            self.print_intodrer(start.right)

    def print_postodrer(self,start):
        if (start is not None) :
            self.print_postodrer(start.left)
            self.print_postodrer(start.right)
            print(start.value)

#------------UTILITARY METHOD OF BINARY TREE------------#

    def size(self,start):
        if(start is None):
            return 0
        else:
            return 1+size(start.left)+size(start.right)

    def max_Depth(self,start):
        if(start is None):
            return 0
        else:
            lDepth = tree.max_Depth(start.left)
            rDepth = tree.max_Depth(start.right)
        if (lDepth > rDepth):
            return(lDepth + 1)
        else:
            return(rDepth + 1)

    def search(self,root,key):
        if root is None or root.value==key:
            return root
        if root.value<key:
            return self.search(root.right,key)
        return self.search(root.left,key)


    def insert(self,root,node):
        if root is None:
            root=node
        else:
            if root.value<node.value:
                if root.right is None:
                    root.right=node
                else:
                    self.insert(root.right,node)
            else:
                if root.left is None:
                    root.left=node
                else:
                    self.insert(root.left,node)
