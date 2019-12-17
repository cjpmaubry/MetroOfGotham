# ----------------------------------------------------------------- IMPORTS ------------------------------------------------------

import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# ----------------------------------------------------------------- PRIM'S ALGORITHM ------------------------------------------------------

# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph
# Part of Cosmos by OpenGenus Foundation
class PrimsAlgorithm():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]

    # Function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        results=np.zeros((10,10))
        print ("Edge \tWeight")
        for i in range(1,self.V):
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ])
            results[i][parent[i]] = self.graph[i][parent[i]]
        return results

    # Function to find the vertex with minimum distance value, from
    # the set of vertices not yet included in shortest path tree
    def minKey(self, key, mstSet):
        # Initilaize min value
        min = 1000000
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    # Function to construct and print MST for a graph represented using
    # adjacency matrix representation
    def primMST(self):
        #Key values used to pick minimum weight edge in cut
        key = [1000000] * self.V
        parent = [None] * self.V # Array to store constructed MST
        key[0] = 0   # Make key 0 so that this vertex is picked as first vertex
        mstSet = [False] * self.V
        parent[0] = -1  # First node is always the root of
        for cout in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
            # Put the minimum distance vertex in the shortest path tree
            mstSet[u] = True
            # Update dist value of the adjacent vertices of the picked vertex
            # only if the current distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
        return self.printMST(parent)


# -------------------------------- DISPLAY -------------------------------- #

#Create the figure with station (edges and vertices)
def Create_Graphs_Network_and_Solution(initial_matrix, result_matrix):  
    plt.figure(figsize=(10,10), dpi=80) # Control the windows dimensions
    G_init = nx.from_numpy_matrix(initial_matrix)
    positions = nx.spring_layout(G_init) # Define coordonate of the station
    nx.draw(G_init,pos = positions,with_labels=True) #Create the Station on the graph and the edge

    plt.figure(figsize=(10,10), dpi=80) # Control the windows dimensions
    G_result = nx.from_numpy_matrix(result_matrix)
    #uses the SAME POSITIONS as INITIAL MATRIX
    nx.draw(G_result,pos = positions, with_labels=True)
    nx.draw_networkx_edge_labels(G_result,pos = positions)

# ----------------------------------------------------------------- MAIN & INITIALIZATION ------------------------------------------------------ #
def main():
    #we have 10 cities in our graph
    g = PrimsAlgorithm(10)

    #matrix of distances
    #Gotham City is the first column, first line
    g.graph = [ [0, 8.1, 9.2, 7.7, 9.3, 2.3, 5.1, 10.2, 6.1, 7],
             [8.1, 0, 12, 0.9, 12, 9.5, 10.1, 12.8, 2, 1],
             [9.2, 12, 0, 11.2, 0.7, 11.1, 8.1, 1.1, 10.5, 11.5],
             [7.7, 0.9, 11.2, 0, 11.2, 9.2, 9.5, 12.0, 1.6, 1.1],
             [9.3, 12.0, 0.7, 11.2, 0, 11.2, 8.5, 1, 10.6, 11.6],
             [2.3, 9.5, 11.1, 9.2, 11.2, 0, 5.6, 12.1, 7.7, 8.5],
             [5.1, 10.1, 8.1, 9.5, 8.5, 5.6, 0, 9.1, 8.3, 9.3],
             [10.2, 12.8, 1.1, 12.0, 1, 12.1, 9.1, 0, 11.4, 12.4],
             [6.1, 2, 10.5, 1.6, 10.6, 7.7, 8.3, 11.4, 0, 1.1],
             [7, 1, 11.5, 1.1, 11.6, 8.5, 9.3, 12.4, 1.1, 0]
           ]

    #matrix de depart convertie en np.matrix
    initial_matrix = np.matrix(g.graph)

    #matrix retournee par prim
    result_matrix = g.primMST()

    #creation des DEUX graphs
    Create_Graphs_Network_and_Solution(initial_matrix,result_matrix)
    plt.show()
    

if __name__ == "__main__":
    main()
