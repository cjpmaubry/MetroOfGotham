# MetroOfGotham
### School project : advanced data structures and algorithms

```
            _____          _     _                               __  __          _
           / ___/   ___   | |_  | |__     __ _   _ __ ___       |  \/  |   ___  | |_   _ __    ___  
          | |  _   / _ \  | __| | '_ \   / _` | | '_ ` _ \      | |\/| |  / _ \ | __| | '__|  / _ \ 
          | |_| | | (_) | | |_  | | | | | (_| | | | | | | |     | |  | | |  __/ | |_  | |    | (_) |
           \____|  \___/   \__| |_| |_|  \__,_| |_| |_| |_|     |_|  |_|  \___|  \__| |_|     \___/ 
  
```
## Spanning tree and pathfinding

Contributors :
- Leopold DUVERGER, @Leoduv
- Corentin AUBRY, @cjpmaubry

# Before Running, IDE and libraries
### IDE and Python version
We used Visual Studio Code in this project Version: 1.41.1 (user setup).
Python version 3.8 was used in this program.
We recommend using the same but you can do it from any IDE supporting at least python 3. 
Be sure if using Visual Studio Code that you have the Python Extention installed ! 

### Pyhton libraries that have to be installed
You can and should run the following lines in your python console in order to intall the needed libraries.
These are all the libraries needed to run the 4 Parts of the project.
```
--> pip install csv
--> pip install math
--> pip install numpy
--> pip install networkx
--> pip install matplotlib
--> pip install pathlib
```

### Download and launch
**If using VS Code** : you can simply clone the projet by doing to flowwing : 

Open Visual Studio Code Go to Top Menu -> Files -> Open Folder Select the folder you would like to download the cloned project

Go to Top Menu -> View -> Integrated Terminal or Terminal

Execute 'git clone' command with the path to the git repository : https://github.com/Leoduv/MetroOfGotham.git

git clone https://github.com/Leoduv/MetroOfGotham.git

If it requires credentials to login then the integrated terminal will ask for username and password.

And here you go the cloned files are already available into the local folder. The you just have to run Part 1, PArt 2 ect to see the different parts of the project.

**If using another IDE** : go on https://github.com/Leoduv/MetroOfGotham and download the zip file.

Create a new reposiroty on your computer and extract the zip into it. You Should have a folder MetroOfGohtam-master where you will see the 4 python files you can execute. Do NOT move the python files from the folder otherwize they won't be able to find the toher files they need.
Just right-click on the python files and open and execute with the desired IDE. 


In both cases make sure that you have the previous python libraries installed.

# Part 1 

## Libraries that have to be installed :
```
--> pip install csv
--> pip install math
--> pip install numpy
--> pip install networkx
--> pip install matplotlib
--> pip install pathlib
```

## Display graph and solution on connected network
We had to extract from the [image](map_gotham_metro.jpg) of the gotham metro network the position of the stations and display a graph with the different connections.
We put by **hand** the information in a [csv file](StationPart1.csv) in order to store the information.
(The coordinates are in Pixels.)

The display of the graphs and solution can be seen in [this file MetroGRaph.py](Part1-MetroGraph.py)

He used the networkx and matplotlib.pyplot libraries in order to create the networks and display them.

### 1-1 Create and display a graph representing the Gotham City’s railways and subways below
Run the file "Part1-MetroGraph". Figure 1 shows the grpah representing the metro with all the lines and stations. In figure 2 the names of the stations are displayed with their corresponding number.

### 1-2 Which kind of algorithm create a connected graph while minimizing the total amount of distance? Show the algorithm? What is its complexity?
The kind of algorithm used is the "Minimum Spanning Tree".The algorith that we are going to use is **Prim's Minimum Spanning Tree**.
It has a complexity of **O(|V|^2)** ( V = vertices).

### 1-3 Show and display a solution of the connected network.
When running "Part1-MetroGraph", figure 3 will display the graph of the solution found by Prim's algorithm.


# Part 2 Shortest Path

## Libraries that have to be installed :
--> pip install numpy

--> pip install networkx

--> pip install matplotlib


### 2-1 Which kind of algorithm create a connected graph while minimizing the distance to a unique city ? What is its complexit?
The algorith we are going to use is **Dijkstra's algorithm ( Dijkstra's Shortest Path First algorithm)**.
It has a complexity of **O((|E|+|V|)*log(|V|))** ( V = vertices and E = edges).

### 2-1 Show and display a solution of the proposed algorithm.
We had to use the matrice given by the subject to run dijktra's algorithm. 
Dijktra's algorithm uses 2 methods : one is used to return the minimum distance between some edges; and the other creates a figure displaying the minmum distance between Gotham and the other towns.

Dijktra's algorithm takes a matrix of connections and returns 2 figures. One displays all the distance between Gotham and the another town and the second figure displays the graph of connection (usefull for the next question).
Note: It's important to notice that in the graph, the values of the node start with 0. Because of that Gotham, which is defined as g0 in the topic appears at node 0 in the figure. Same for g1 appears at node 1 etc...

### 2-3 Show and display a solution of the problem
As we can see with the figure 1 generated by the Dijktra's algorithm, there are **7 leafs** on the graph. So we can say, it's necessary to send **7 volunteers.**

Note : We can see in the matrix given in the topic that go to city G4 directly from G1 or from G1 then G9, this is the same distance value (7,7). But the algorithm returns the path G1-G9-G4 because it's better in term of volunteers number.
(The algorithm first checks direct connections from G1 to the other and after it checks undirect connections. By doing that, if an undirect connection has the same distance, it will take the undirect connection to minimize the number of volunteers needed !)

# Part 3

## Libraries that have to be installed :
--> pip install csv

--> pip install pathlib

#### Dataset created
In this part we use a dataset composued of thr ID of a member, the name of that member, and the id of the member that certified him.

### 3-1 Suggest and show a greedy method to find an ID in a (linear) database. What is its complexity ?
We used an algorithm that scans the entire dataset **element by element** to find the ID (it stops as soon as it finds it).
It has a complexity of **O(n)**.
The database is in the file called "DatasetPart3.csv " (ID,Name,IDofconfirmed). It stores the ID and the name of the member and the Id of the member that certified this member.
Note : In this dataset the Id is already sorted (Automaticaly sorted when the CSV was created), but the methode FindID also works for unsorted data.

### 3-2 Suggest and show a divide and conquer method to find an ID in a (linear) database. What is its complexity ?
Because for the moment we use a sorted database we decided to use the method of a **dichotomic search** algorithm.
It has a complexity of **O(log(n))**
Note : Both research algorithms search the ID of a member in the dataset. If the ID is in the dataset, the algorithm displays in the console a message informing the ID is in the Dataset, the name of the member and also the name of the member that certified him.

### 3-3 Suggest and show a method that sort the (linear) database and find an ID. What is its complexity ?
First we decided to use another dataset named "DatasetPart3NotSort.csv" : we modified the order of the elements to "unsort" the IDs. In that way we can apply the sort method.
We decide to use the sort algorithm **merge sort.** 
It has a complexity of **O(nlog(n))**

### 3-4 Show and display the three methods with an example of database of your choice (at least 50 data)
We decided to use the unsorted database ( DatasetPart3NotSort.csv).
We first call the main launch the FindID method (Question 3-1), which displays the research of the ID number 10.
Secondly it launches the **sort method** (in order to apply the dichotomic search after).
Finally it launches the **dichotomic search algorithm** for the ID number 12.
All the ID numbers could be changed in the mainif you want to test with other. 

# Part 4
## Libraries that have to be installed :
--> pip install csv

--> pip install pathlib

## Dataset used
In this final part, the work was focused on tree manipulation. We had to create a dataset of our choice and use it.
We decided to used a list of the names of members, but **crypted** : the names are written in ASCII.
The program taked a csv file containing the names of Jocker's members and then saves the names in a list but by applying a methode that takes the name and return the **ASCII version of the name**.

This allows us to have a dataset composed of numbers, meaning that we will be able to build trees that need to compare values. our dataset contains 100 names.

### 4-1 Suggest and show a method to manage a database in a binary tree; present a method to find any value in the tree (show both complexity). Show the methods with your own example (at least 50 data).
We crated a simple binary tree with two classes "Node" and "BinaryTree". In a simple Binary Tree, a node can have maximum two children. Inserting an element has a complexity of **O(n)**, and searching for an element also is **O(n)**. But we did a **Binary Search Tree**, where the left child of a node has value less than the parent and right child has value greater than parent. This still means that in the worst cases it has a time complexity of **O(n)** in searching and inserting, but has a **general time complexity is O(h)** where h is height of the tree.

### 4-2 Suggest and show a method to improve the database management thanks to the works of the soviets Adelson-Velsky and Landis with the previous database.
A way to inprove the database management is to use and **AVL tree** instead. This king of tree reuses the propreties of a Binary Search tree but now difference between height of left sub-tree and right sub-tree of any node can’t be more than 1. It will auto balance itself when inserting new data by performing **rotations**. 

We reused the classes from the BST but added a **new insertion method** in order to create a AVL. This tree allows to reduce the time complexity which is now a worst case complexity of **O(log2n)**.

### 4-3 Suggest and show a method that sort the database un a tree where the node can store multiple value like the works of Bayer and McCreight. Take your own example (at least 100 data) where each node can store up to 5 values.
In order to create a tree capable of storing multiple values in each node, wa decided to create a **BTree**.
The tree follows the works if Bayer and McCreight, and in our case we had to ba able to store up to **5 values per node, so U = 5+1**.
Since U = 6, and U = t * 2, we knew that the **minimum degree** of our tree should be t = 3.
We had to create two new classes in order to implement this kind of tree, BTreeNode and BTree.

The nodes can contain up to 5 values, and when a child or node is full of values, a method will split thqt child into two new nodes. The bottom part of the tree will have more values and children per node than the upper part.

We decided to display the tree in order just to show that everything is in the correct place.

