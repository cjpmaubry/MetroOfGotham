# ----------------------------------------------------------------- IMPORT PART ------------------------------------------------------

import csv
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


# ----------------------------------------------------------------- METHODS ------------------------------------------------------

# ----------------------------- DATASET CONSTRUCTION ----------------------------- #
#Get the csv file and create a dataset with it
def GiveDataSetStation():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "Station.csv"
    with open(file_to_open, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
    return dataset

#Get the csv file and create a dataset with it
def GiveDataSetEdge():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "Edge.csv"
    with open(file_to_open, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset=list(lines)
    return dataset


#Creates Matrix of connection (Edges) using the dataset
def CreateMatrix(datasetStation,datasetEdge):
    matrix=np.zeros((90,90))
    listconnection=DefineConnection(datasetStation,datasetEdge)
    a=len(listconnection)
    for tab in range (0,len(listconnection)):
        matrix[int(listconnection[tab][0])-1][int(listconnection[tab][1])-1] = float(listconnection[tab][2])
    return matrix

#Creates a list which includes all the connections (Edges) between the Station
def DefineConnection(datasetStation,datasetEdge):  
    listconnection=[]
    for i in range(0,len(datasetEdge)):  
        #Browse all lines  
        tab2=[datasetEdge[i][0],datasetEdge[i][1],getDistance(datasetEdge[i][0],datasetEdge[i][1],datasetStation),datasetEdge[i][2]]
        listconnection.append(tab2)             
    return listconnection


#Give the euclidian distance between 2 Stations of a dataset
def getDistance(indice1,indice2,dataset):
    distance =0
    for x in range(2,4): #  on a 2 dimensions
        distance += pow((float(dataset[int(indice1)-1][x])-float(dataset[int(indice2)-1][x])),2)
    return round(math.sqrt(distance)) # Return the round distance ( to have a better look in the figure)

#Returns the id and position of the stations in a dict ( use a dataset to find the info)
def ExtractionCoordonateOfStation(dataset):
    #initialises empty dict
    positions_dict = {0: (0,0)}
    for k in range(0,len(dataset)):
        #Browse all lines
        positions_dict[int(dataset[k][0])-1] = (int(dataset[k][2]), int(dataset[k][3]))
    return positions_dict


# ----------------------------- CREATION AND DISPLAY OF GRAPHS  ---------------------------- #
#Creates a matix of the vertices and then displays the graph associated
def DrawGraphs(datasetStation,datasetEdge):
    positions_dict = ExtractionCoordonateOfStation(datasetStation)
    positions = positions_dict
    A = CreateMatrix(datasetStation,datasetEdge) # Recovery the matrix of connection
    #Define graphical parametres
    CreateGraphStation(A,positions,datasetStation,datasetEdge) #Create the figure with station (edges and vertices)
    DisplayNameStation(datasetStation) # Create other figure to display the name of the station
    plt.show() # Display the Graphs 


#Create the figure with station (edges and vertices)
def  CreateGraphStation(A,positions,datasetStation,datasetEdge):  
    plt.figure(figsize=(10,10), dpi=80) # Control the windows dimensions
    G = nx.from_numpy_matrix(A)
    pos=nx.spring_layout(G) # Define coordonate of the station    
    nx.draw_networkx(G,pos = positions,with_labels=True) #Create the Station on the graph and the edge
    edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])# Define the label of the edges
    nx.draw_networkx_edge_labels(G,pos= positions,font_size=8,edge_labels=edge_labels) #Added on graph the weight of each edge
    
    # Added color of the line in the graph
    R= nx.from_numpy_matrix(GiveLine('r',datasetStation,datasetEdge))
    nx.draw_networkx_edges(R,pos= positions,font_size=7,edge_color='r',width=4)
    B= nx.from_numpy_matrix(GiveLine('b',datasetStation,datasetEdge))
    nx.draw_networkx_edges(B,pos= positions,font_size=7,edge_color='b',width=4)
    N= nx.from_numpy_matrix(GiveLine('k',datasetStation,datasetEdge))
    nx.draw_networkx_edges(N,pos= positions,font_size=7,edge_color='k',width=4)
    Y= nx.from_numpy_matrix(GiveLine('y',datasetStation,datasetEdge))
    nx.draw_networkx_edges(Y,pos= positions,font_size=7,edge_color='y',width=4)
    M= nx.from_numpy_matrix(GiveLine('m',datasetStation,datasetEdge))
    nx.draw_networkx_edges(M,pos= positions,font_size=7,edge_color='m',width=4)
    C= nx.from_numpy_matrix(GiveLine('c',datasetStation,datasetEdge))
    nx.draw_networkx_edges(C,pos= positions,font_size=7,edge_color='c',width=4)
    G= nx.from_numpy_matrix(GiveLine('g',datasetStation,datasetEdge))
    nx.draw_networkx_edges(G,pos= positions,font_size=7,edge_color='g',width=4)


#Method which give the matrix of connection for a specific line (color)
def GiveLine(color,datasetStation,datasetEdge):
    matrix=np.zeros((90,90))
    listconnection=DefineConnection(datasetStation,datasetEdge)
    a=len(listconnection)
    for tab in range (0,len(listconnection)):
        if(datasetEdge[tab][2]==color):
            matrix[int(listconnection[tab][0])-1][int(listconnection[tab][1])-1] = float(listconnection[tab][2])
    return matrix



#Create a plot with the name of the Station
def DisplayNameStation(dataset):
    plt.figure(figsize=(5,9), dpi=90)# Control the windows dimensions
    plt.axis([0, 20, 0, 90])  
    for k in range(0,len(dataset)): 
        #Browse all lines
        idstation=int(dataset[k][0])-1
        name=dataset[k][1]
        plt.text(6, 90-k, idstation,fontsize=6)
        plt.text(8, 90-k, name,fontsize=6)
    plt.axis('off') # Hide the axes
    plt.title("List of station with their ID") # Write title
    
# ----------------------------------------------------------------- MAIN ------------------------------------------------------


def main():
    datasetStation=GiveDataSetStation()
    datasetEdge=GiveDataSetEdge()
    DrawGraphs(datasetStation,datasetEdge)


if __name__ == "__main__":
    main()