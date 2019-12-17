# ----------------------------------------------------------------- IMPORT PART ------------------------------------------------------

import csv
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------------------------------------------- METHOD PART ------------------------------------------------------


#Returns the id and position of the stations in a dict ( use a dataset to find the info)
def ExtractionCoordonateOfStation(dataset):
    #initialises empty dict
    positions_dict = {0: (0,0)}
    for k in range(1,91): # begin at 1 to skip the first line / 91 for the number of line in csv
        #Browse all lines
        positions_dict[int(dataset[k][0]) - 1] = (int(dataset[k][2]), int(dataset[k][3]))
    return positions_dict


#Creates a matix of the vertices and then displays the graph associated
def DrawGraphs(dataset):
    positions_dict = ExtractionCoordonateOfStation(dataset)
    positions = positions_dict
    A = CreateMatrix(dataset) # Recovery the matrix of connection
    #Define graphical parametres
    CreateGraphStation(A,positions) #Create the figure with station (edges and vertices)
    DisplayNameStation(dataset) # Create other figure to display the name of the station
    plt.show() # Display the Graphs 


#Create the figure with station (edges and vertices)
def  CreateGraphStation(A,positions):  
    plt.figure(figsize=(10,10), dpi=80) # Control the windows dimensions
    G = nx.from_numpy_matrix(A)
    pos=nx.spring_layout(G) # Define coordonate of the station
    nx.draw(G,pos = positions,with_labels=True) #Create the Station on the graph and the edge
    

#Give the euclidian distance between 2 Stations of a dataset
def getDistance(indice1,indice2,dataset):
    distance =0
    for x in range(2,4): #  on a 2 dimensions
        distance += pow((float(dataset[int(indice1)][x])-float(dataset[int(indice2)][x])),2)
    return math.sqrt(distance)


#Get the csv file and create a dataset with it
def GiveDataSet():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "Station.csv"
    with open(file_to_open, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
    return dataset



#Create a list which includes all the connection (the edges) between the Station
def DefineConnection(dataset):  
    listconnection=[]
    for i in range(1,91): # begin at 1 to skip the first line 
        #Browse all lines  
        tab=FindTheConnection(dataset[i][4])
        for k in range(0,len(tab)):
            tab2=[dataset[i][0],tab[k],getDistance(dataset[i][0],tab[k],dataset)]
            listconnection.append(tab2)  
    a=len(listconnection)           
    return listconnection


#Split the string using as separator ";"
def FindTheConnection(string):
    tab=string.split(';')
    return tab


#Create Matrix of connection using the dataset
def CreateMatrix(dataset):
    matrix=np.zeros((90,90))
    listconnection=DefineConnection(dataset)
    a=len(listconnection)
    for tab in range (0,len(listconnection)):
        matrix[int(listconnection[tab][0])-1][int(listconnection[tab][1])-1] = float(listconnection[tab][2])
    return matrix


#Create a plot with the name of the Station
def DisplayNameStation(dataset):
    plt.figure(figsize=(5,9), dpi=90)# Control the windows dimensions
    plt.axis([0, 20, 0, 90])  
    for k in range(1,91): # begin at 1 to skip the first line / 91 for the number of line in csv
        #Browse all lines
        idstation=int(dataset[k][0])-1
        name=dataset[k][1]
        plt.text(6, 90-k, idstation,fontsize=6)
        plt.text(8, 90-k, name,fontsize=6)
    plt.axis('off') # Hide the axes
    plt.title("List of station with their ID") # Write title
    
# ----------------------------------------------------------------- MAIN ------------------------------------------------------


def main():
    dataset=GiveDataSet()
    DrawGraphs(dataset)


if __name__ == "__main__":
    main()