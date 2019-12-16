import csv
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

#Returns the id and position of the stations in a dict ( use a dataset to find the info)
def ExtractionCoordonateOfStation(dataset):
    #initialises empty dict
    positions_dict = {0: (0,0)}
    for k in range(1,91): # begin at 1 to skip the first line / 91 for the number of line in csv
        #Browse all lines
        positions_dict[int(dataset[k][0]) - 1] = (int(dataset[k][2]), int(dataset[k][3]))
        #print(int(dataset[k][0]) - 1, " : ", positions_dict[int(dataset[k][0]) - 1])
    return positions_dict

#Creates a matix of the vertices and then displays the graph associated
def DrawGraph(dataset):

    positions_dict = ExtractionCoordonateOfStation(dataset)
    testing_positions = positions_dict

    A = CreateMatrix(dataset) # Recovery the matrix of connection


    G = nx.from_numpy_matrix(A)
    pos=nx.spring_layout(G) # Define coordonate of the station
    nx.draw(G,pos = testing_positions,with_labels=True) #Create the Station on the graph and the edge
    #nx.draw_networkx_edge_labels(G,pos)
    plt.show() # Display the Graph


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


def CreateMatrix(dataset):
    matrix=np.zeros((90,90))
    listconnection=DefineConnection(dataset)
    a=len(listconnection)
    for tab in range (0,len(listconnection)):
        matrix[int(listconnection[tab][0])-1][int(listconnection[tab][1])-1] = float(listconnection[tab][2])
    return matrix



def main():
    dataset=GiveDataSet()
    DrawGraph(dataset)

if __name__ == "__main__":
    main()