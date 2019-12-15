import csv
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

#Returns the id and position of the stations in a dict ( use a dataset to find the info)
def ExtractionInfoFromFile(dataset):
    #initialises empty dict
    positions_dict = {0: (0,0)}
    for k in range(1,91): # begin at 1 to skip the first line / 91 for the number of line in csv
        #Browse all lines
        positions_dict[int(dataset[k][0]) - 1] = (int(dataset[k][2]), int(dataset[k][3]))
        print(int(dataset[k][0]) - 1, " : ", positions_dict[int(dataset[k][0]) - 1])
    return positions_dict

#Creates a matix of the vertices and then displays the graph associated
def DrawGraph():

    testing_positions = {0: (10, 10), 1: (30, 15), 2: (10, 30), 3: (20, 20), 4: (100,150)}

    A = np.matrix([ [0, 2, 0, 6, 0],
                [2, 0, 3, 8, 5],
                [0, 3, 0, 0, 7],
                [6, 8, 0, 0, 9],
                [0, 5, 7, 9, 0]])

    #waiting commetns from @cpjmaubry
    G = nx.from_numpy_matrix(A)
    pos=nx.spring_layout(G)
    nx.draw(G,pos = testing_positions,with_labels=True)
    nx.draw_networkx_edge_labels(G,pos)
    plt.show()


def getDistance(indice1,indice2,dataset):
    distance =0
    for x in range(2,4): #  on a 2 dimensions
        distance += pow((float(dataset[int(indice1)][x])-float(dataset[int(indice2)][x])),2)
    return math.sqrt(distance)


def GiveDataSet():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "Station.csv"
    with open(file_to_open, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
    return dataset




def DefineConnection(dataset):  
    listconnection=[]
    for i in range(1,91): # begin at 1 to skip the first line 
        #Browse all lines  
        tab=FindTheConnection(dataset[i][4])
        for k in range(0,len(tab)):
            tab2=[dataset[i][0],tab[k],getDistance(dataset[i][0],tab[k],dataset)]
            listconnection.append(tab2)           
    
    return listconnection



#Split the string using as separator ";"
def FindTheConnection(string):
    tab=string.split(';')
    return tab


def main():
    dataset=GiveDataSet()
    DefineConnection(dataset)
    ExtractionInfoFromFile(dataset)

if __name__ == "__main__":
    main()