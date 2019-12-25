
import csv
from pathlib import Path


class BTreeNode(object):
    """A B-Tree Node.
    
    attributes
    =====================
    leaf : boolean, determines whether this node is a leaf.
    keys : list, a list of keys internal to this node
    c : list, a list of children of this node
    """
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.c    = []
        
    def __str__(self):
        if self.leaf:
            return "Leaf BTreeNode with {0} keys\n\tK:{1}\n\tC:{2}\n".format(len(self.keys), self.keys, self.c)
        else:
            return "Internal BTreeNode with {0} keys, {1} children\n\tK:{2}\n\n".format(len(self.keys), len(self.c), self.keys, self.c)


class BTree(object):
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t    = t
    
    def search(self, k, x=None):
        """Search the B-Tree for the key k.
        
        args
        =====================
        k : Key to search for
        x : (optional) Node at which to begin search. Can be None, in which case the entire tree is searched.
        
        """
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:    # look for index of k
                i += 1
            if i < len(x.keys) and k == x.keys[i]:       # found exact match
                return (x, i)
            elif x.leaf:                                # no match in keys, and is leaf ==> no match exists
                return None
            else:                                       # search children
                return self.search(k, x.c[i])
        else:                                           # no node provided, search root of tree
            return self.search(k, self.root)
        
    def insert(self, k):
        r = self.root
        if len(r.keys) == (2*self.t) - 1:     # keys are full, so we must split
            s         = BTreeNode()
            self.root = s
            s.c.insert(0, r)                  # former root is now 0th child of new root s
            self._split_child(s, 0)            
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)
    
    def _insert_nonfull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf: #/// HERE IS THE ERROR 
            # insert a key
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            # insert a child
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            #CODE QUE J'AI RAJOUTE
            if(len(x.c)<i+1):
                s = BTreeNode()
                s.keys.append(k)
                x.c.append(s)
            else:
            #FIN CODE QUE J'AI RAJOUTE              
                if len(x.c[i].keys) == (2*self.t) - 1:
                    self._split_child(x, i)
                    if k > x.keys[i]:
                        i += 1
                self._insert_nonfull(x.c[i], k)
        
    def _split_child(self, x, i):
        t = self.t
        y = x.c[i]
        z = BTreeNode(leaf=y.leaf)
        
        # slide all children of x to the right and insert z at i+1.
        x.c.insert(i+1, z)
        x.keys.insert(i, y.keys[t-1])
        
        # keys of z are t to 2t - 1,
        # y is then 0 to t-2
        z.keys = y.keys[t:(2*t - 1)]
        y.keys = y.keys[0:(t-1)]
        
        # children of z are t to 2t els of y.c
        if not y.leaf:
            z.c = y.c[t:(2*t)]
            y.c = y.c[0:(t-1)]    
        
    def __str__(self):
        r = self.root
        return r.__str__() + '\n'.join([child.__str__() for child in r.c])  




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


def CreateBtree(dataset):
    Btree=BTree(3)
    for k in range(0,len(dataset)):
        Btree.insert(FromNameToAscii(dataset[k][0]))
    return Btree

def GiveDataSetMembers():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "Members.csv"
    with open(file_to_open, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
    return dataset







def main():
    dataset=GiveDataSetMembers()
    Btree=CreateBtree(dataset)


if __name__ == "__main__":
    main()


