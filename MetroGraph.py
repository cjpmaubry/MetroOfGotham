import csv
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

#Reads a CSV file containing the information on the positions and connections of the stations
#Returns the id and position of the stations in a dict
def ExtractionInfoFromFile():
    #finding the folder and file
    data_folder = Path("MetroOfGotham/")
    file_to_open = data_folder / "Station.csv"

    file = open(file_to_open, "r")

    #initialises empty dict
    positions_dict = {0: (0,0)}

    try:
        reader = csv.reader(file)
        #skips the header
        next(reader)
        for row in reader:
            #fills the dict
            positions_dict[int(row[0]) - 1] = (int(row[2]), int(row[3]))
            print(int(row[0]) - 1, " : ", positions_dict[int(row[0]) - 1])

    finally:
        file.close()
    return positions_dict

#Creates a matix of the vertices and then displays the graph associated
def DrawGraph():
    position_of_vertices = ExtractionInfoFromFile()
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
    for x in range(1): # de 0 à 1 car on a 2 dimensions
        distance += pow((float(dataset[indice1][x+1])-float(dataset[indice2][x+1])),2)
    return math.sqrt(distance)


def main():
    DrawGraph()

if __name__ == "__main__":
    main()