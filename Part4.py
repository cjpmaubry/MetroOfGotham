
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
            self.print_preodrer(start.left)
            self.print_preodrer(start.right)

    def print_inorder(self,start):
        if (start is not None) :
            self.print_intodrer(start.left)
            print(start.value)
            self.print_intodrer(start.right)

    def print_postorder(self,start):
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


def main():
    dataset=GiveDataSetMembers()
    tree=CreateTree(dataset)
    tree.print_inordrer(tree.root)

if __name__ == "__main__":
    main()