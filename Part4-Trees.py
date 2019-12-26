
import csv
from pathlib import Path



#------------------------------------------------------------DATASET------------------------------------------------------------#
def GiveDataSetMembers():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "MembersPart4.csv"
    with open(file_to_open, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
    return dataset

#---------------Crypting and uncryting of the names---------------#

#Returns the ascii value of the string "name"
def FromNameToAscii(name):
    crypted_name = 0
    offset = 1000
    len_name = len(name)
    position = 0
    for letter in name:
        if position <= len_name:
            crypted_name += ord(name[position]) * pow(offset, len_name - position - 1)
            position += 1
    return crypted_name

#Returns the string of the "crypted" ascii 
def FromAsciiToName(crypted):
    name = ""
    offset = 1000
    index = 0
    #finds the length of the word to recreate
    if len(str(crypted)) % 3 == 0:
        number_letters = int(len(str(crypted)) / 3)
    else:
        number_letters = int((len(str(crypted)) + 1) / 3)

    #adds each letter to the name
    for index in range(number_letters):
        letter = int(crypted / pow(offset, number_letters - index - 1))
        #"substracts" the letter once its ascii value has been stored in "letter"
        crypted -= letter * pow(offset, number_letters - index - 1)
        #adds that letter to the word
        name += chr(letter % pow(offset, number_letters - index))
        index += 1
    return name











#------------------------------------------------------BINARY TREE------------------------------------------------------#
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

    def print_preorder(self,start):
        if (start is not None) :
            print(start.value)
            self.print_preorder(start.left)
            self.print_preorder(start.right)

    def print_inorder(self,start):
        if (start is not None) :
            self.print_inorder(start.left)
            print(start.value)
            self.print_inorder(start.right)

    def print_postorder(self,start):
        if (start is not None) :
            self.print_postorder(start.left)
            self.print_postorder(start.right)
            print(start.value)

#------------UTILITARY METHOD OF BINARY TREE------------#
    #returns the size of the tree
    def size(self,start):
        if(start is None):
            return 0
        else:
            return 1+size(start.left)+size(start.right)

    #searches for a value in the tree
    def search(self,root,key):
        if root is None or root.value==key:
            return root
        if root.value<key:
            return self.search(root.right,key)
        return self.search(root.left,key)

    #insert a new value in the tree, used to create it
    def insert(self,root,node):
        if root is None:
            root=node
        else:
            #smaller values go left and bigger go right
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

    #search in binary trees
    def SearchName(self,name):
        key=FromNameToAscii(name)
        node=self.search(self.root,key)
        if(node is None):
            print("This name isn't in the database")
        else:
            print("This name is in the database")
            print(node.value)
            print(FromAsciiToName(node.value))









#------------------------------------------------------AVL TREE------------------------------------------------------#
#Uses the same class as binary tree since an AVl is a binary tree but the big difference is in the insertion and creation
    #returns the height
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1

    #returns true is the tree is balanced 
    def isBalanced(self,root):
        if root is None:
            return True
        lh=self.height(root.left)
        rh=self.height(root.right)
        if(abs(lh-rh)<=1)and self.isBalanced(root.right) is True and self.isBalanced(root.left) is True:
            return True
        return False

    #inserts a value in the tree
    #insures that the tree remains balanced and does rotations in order to correct itself
    def insert_AVL(self,root,key):
        if not root:
            return key
        elif key.value < root.value:
            root.left=self.insert_AVL(root.left,key)
        else:
            root.right=self.insert_AVL(root.right,key)
        # Updates the height of the ancestor node
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        # Gets the balance factor
        balance=self.getBalance(root)

        # If the node is unbalanced, then tries out 4 possible cases
        #Case 1 - Left Left
        if balance >1 and key.value <root.left.value:
            return self.RightRotate(root)
        #Case 2 - Right Right
        if balance <-1 and key.value >root.right.value:
            return self.LeftRotate(root)
        #Case 3 - Left Right
        if balance >1 and key.value >root.left.value:
            root.left=self.LeftRotate(root.left)
            return self.RightRotate(root)
        #Case 4 - Right Left
        if balance <-1 and key.value <root.right.value:
            root.right=self.RightRotate(root.right)
            return self.LeftRotate(root)

        return root

    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getHeight(self,root):
        if not root:
            return 0
        return self.height(root)

    #left rotation
    def LeftRotate(self,z):
        y=z.right
        T2=y.left

        #perform rotation
        y.left=z
        z.right=T2

        #update heights
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))

       #return the new root
        return y

    #right rotation
    def RightRotate(self,z):
        y=z.left
        T2=y.right

        #Perform rotation
        y.right=z
        z.left=T2

        #update heights
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))

        #return the new root
        return y








#------------------------------------------------------B-TREE------------------------------------------------------#
##A new class was needed for the BTree since a node can now store multiple values
#and have multiple children
class BTreeNode(object):

    def __init__(self, leaf=False):
        self.leaf = leaf #boolean, true is the node is a leaf
        self.values = [] #list of the values stored in the node
        self.c    = [] #list of children of this node


class BTree(object):
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t    = t #minimum degree of the tree
        #U = T * 2
        #We need to store a maximum of 5 values per node
        #In our case U = 5+1 and t = 3

    #prints the values stored in order
    def BTree_print_inorder(self,start):
        if (start.leaf is not True) :
            index = 0
            for node in start.c:             
                self.BTree_print_inorder(start.c[index])
                #prints one value after printing what values are stored in the child associated
                if index < len(start.values):
                    print(start.values[index])
                    index += 1

        #if it is a leaf, prints all the value stored in the node
        if (start.leaf is True) :
            for val in range(0,len(start.values)):
                print(start.values[val])

    #Searches a given value in the tree
    def BTree_search(self, val, x=None):
        #val : searched name
        #x : start node, here None so that we search in the whole tree.
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.values) and val > x.values[i]:
                i += 1 #finds index of the value
            #if it finds a match
            if i < len(x.values) and val == x.values[i]:
                return FromAsciiToName(x.values[i])

            elif x.leaf:
                #if no match if found and its a leaf : value not in tree                               
                return None
            else:       
                #if nothing found, moves to children
                return self.BTree_search(val, x.c[i])
        else:  
            #if we dont give him a starting point, starts at the root                                         
            return self.BTree_search(val, self.root)
    
    #inserts a value in the Btree, splitting when needed
    def insert(self, val):
        r = self.root

        #if the values are full, we split
        if len(r.values) == (2*self.t) - 1:
            spt = BTreeNode()
            self.root = spt
            spt.c.insert(0, r)  #previous root is now the child 0 of the new one
            self._split_child(spt, 0)            
            self._insert_nonfull(spt, val)
        else:
            self._insert_nonfull(r, val)
    
    #inserts in a node that isnt full of values already
    def _insert_nonfull(self, x, val):
        i = len(x.values) - 1
        if x.leaf: 
            # if its a leaf, simply inserts the value
            x.values.append(0)
            while i >= 0 and val < x.values[i]:
                x.values[i+1] = x.values[i]
                i -= 1
            x.values[i+1] = val
        else:
            # if its not, inserts a child
            while i >= 0 and val < x.values[i]:
                i -= 1
            i += 1
            # adds the value to the child
            if(len(x.c)<i+1):
                s = BTreeNode()
                s.values.append(val)
                x.c.append(s)
            else:
            # splits if needed             
                if len(x.c[i].values) == (2*self.t) - 1:
                    self._split_child(x, i)
                    if val > x.values[i]:
                        i += 1
                self._insert_nonfull(x.c[i], val)
    
    #splits a node into two other nodes
    #the "middle" value is return to the parent
    #HAS to be called on full nodes
    def _split_child(self, x, i):
        t = self.t
        y = x.c[i]
        z = BTreeNode(leaf=y.leaf)
        
        # puts all children of x to the right and inserts z at i+1.
        x.c.insert(i+1, z)
        x.values.insert(i, y.values[t-1])
        
        # values of z are founf from t to 2t - 1,
        # values of y are then from 0 to t-2
        z.values = y.values[t:(2*t - 1)]
        y.values = y.values[0:(t-1)]
        
        # children of z are from t to 2t
        if not y.leaf:
            z.c = y.c[t:(2*t)]
            y.c = y.c[0:(t)]   

    def PrintALeaf(self, start):
        while start.leaf is not True:
            start = start.c[0]
            self.PrintALeaf(start)
        return "Number of values stored in this leaf : {0}".format(len(start.values))






                        






#----------------------------------QUESTION-1-BinaryTree--------------------------------------#

def CreateTree(dataset):
    tree=BinaryTree(FromNameToAscii(dataset[0][0]))
    for k in range(1,len(dataset)):
        tree.insert(tree.root,Node(FromNameToAscii(dataset[k][0])))
    return tree


#----------------------------------QUESTION-2-AVL--------------------------------------#

    
def CreateAVL(dataset):
    AVL=BinaryTree(FromNameToAscii(dataset[0][0]))
    for k in range(1,len(dataset)):
        AVL.root = AVL.insert_AVL(AVL.root,Node(FromNameToAscii(dataset[k][0])))
    return AVL


#----------------------------------QUESTION-3-Btree-------------------------------------#

    
def CreateBtree(dataset):
    Btree=BTree(3)
    for k in range(0,len(dataset)):
        Btree.insert(FromNameToAscii(dataset[k][0]))
    return Btree


#------------------------------------------------------------MAIN------------------------------------------------------------#

def main():
    dataset = GiveDataSetMembers()

    #Question 1 - Binary Tree
    tree=CreateTree(dataset)
    tree.print_inorder(tree.root)
    print("That was Binary Tree In Order \n")
    print("We searched for Daniel_JACKSON in our tree :")
    tree.SearchName('Daniel_JACKSON')
    print("press enter to see AVL version")
    input()

    #Question 2 - AVL
    AVL=CreateAVL(dataset)
    AVL.print_inorder(AVL.root)
    print("That was AVL Tree In Order \n")
    print("We searched for Daniel_JACKSON in our AVL tree :")
    AVL.SearchName('Daniel_JACKSON')
    print("press enter to see B-tree version")
    input()

    #Question 3 - BTree
    members_Btree=CreateBtree(dataset)
    members_Btree.BTree_print_inorder(members_Btree.root)
    print("That was B-tree Tree In Order \n")
    print("Just to proove that its a BTree, here is the number of values stored in the far left leaf")
    print(members_Btree.PrintALeaf(members_Btree.root))
    print("\nWe searched for Daniel_JACKSON in our Btree")
    search_result = members_Btree.BTree_search(FromNameToAscii('Daniel_JACKSON'))
    print("If his ID is in the tree his name will be printed :")
    print(search_result)
    print("press enter to finish")
    input()

if __name__ == "__main__":
    main()