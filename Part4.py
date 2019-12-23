
import csv
from pathlib import Path


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

    def size(self,start):
        if(start is None):
            return 0
        else:
            return 1+size(start.left)+size(start.right)


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

                        


#------------------------------------------------------------DATASET------------------------------------------------------------#

def CreateTree(dataset):
    tree=BinaryTree(FromNameToAscii(dataset[0][0]))
    for k in range(1,len(dataset)):
        tree.insert(tree.root,Node(FromNameToAscii(dataset[k][0])))
    return tree


def GiveDataSetMembers():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "Members.csv"
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


def SearchName(tree,name):
    key=FromNameToAscii(name)
    node=tree.search(tree.root,key)
    if(node is None):
        print("This name isn't in the database")
    else:
        print("This name is in the database")
        print(node.value)
        print(FromAsciiToName(node.value))


#----------------------------------QUESTION--AVL--------------------------------------#

    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1


    def isBalanced(self,root):
        if root is None:
            return True
        lh=self.height(root.left)
        rh=self.height(root.right)
        if(abs(lh-rh)<=1)and self.isBalanced(root.right) is True and self.isBalanced(root.left) is True:
            return True
        return False


    def insert_AVL(self,root,key):

        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left=self.insert_AVL(root.left,key)
        else:
            root.right=self.insert_AVL(root.right,key)
        # Update the height of the ancestor node
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        # Get the balance factor
        balance=self.getBalance(root)

        # If the node is unbalanced, then try out 4 cases
        #Case 1 - Left Left
        if balance >1 and key <root.left.val:
            return self.rightRotate(root)
        #Case 2 - Right Right
        if balance <-1 and key >root.right.val:
            return self.leftRotate(root)
        #Case 3 - Left Right
        if balance >1 and key>root.left.val:
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        #Case 4 - Right Left
        if balance <-1 and key<root.right.val:
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)

        return root



    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)


    def getHeight(self,root):
        if not root:
            return 0
        return root.height


    def LeftRotate(self,z):

        y=z.right
        T2=y.left

        #Perform rotation
        y.left=z
        z.right=T2

        #update heights
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))

        #return the new root
        return y



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






#-----------------------------------------MAIN-----------------------------------------#

def main():
    dataset=GiveDataSetMembers()
    tree=CreateTree(dataset)
    #tree.print_inorder(tree.root)
    SearchName(tree,'Daniel_JACKSON')
    

if __name__ == "__main__":
    main()