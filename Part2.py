
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


#-----------------DEFINE STRUCTURE OF GRAPH --------------------#

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  

#------------------UTILITARY FONCTION-------------------#

    def PrintSolution(self, dist): 
        print ("Vertex \tDistance from Source (vertex 1)")
        for node in range(self.V): 
            print (node+1, "\t", dist[node] )
  

    # This method finds the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree 
    def MinimumDistance(self, dist, ListeofVertice): 
  
        # initialize minimum distance for next node 
        min = 9999999999999999 # Set a big number to initialize
  
        # Loop to browse all the connection for a specific vertex
        for v in range(self.V): 
            if dist[v] < min and ListeofVertice[v] == False: # Define condition to return to minimum distance from this vertex to another
                min = dist[v] 
                min_index = v 
  
        return min_index 


#------------Dijkstra Algorithm------------#

    # Method that implements Dijkstra's alghorithm  ( start is the vertex for the shortest path)
    def Dijkstra(self, start): 
        matrix=np.zeros((10,10))
        distance = [9999999999999] * self.V  # Set a big number to initialize 
        distance[start] = 0 #Initialise the start distance
        ListeofVertice = [False] * self.V 
  
        for count in range(self.V): 
  
            # Pick the minimum distance vertex from the set of vertices not yet processed.  
            u = self.MinimumDistance(distance, ListeofVertice) 
  
            # Put the minimum distance vertex in the shortest path tree
            ListeofVertice[u] = True

            #Begin the loop to update the distance between vertex for the shortest path and only for  the shortest path
            for v in range(self.V): 
                if self.graph[u][v] > 0 and ListeofVertice[v] == False and distance[v] > distance[u] + self.graph[u][v]: #Verify the condition
                        distance[v] = distance[u] + self.graph[u][v]
                        #Loop to remove old value of distance, the old path when a better is found
                        for k in range(0,9):
                            matrix[k][v]=0
                        matrix[u][v]=distance[v]
                        
  
        plt.figure(figsize=(8,8), dpi=80)
        plt.title("Dijktra Graph")
        G_result = nx.from_numpy_matrix(matrix)
        nx.draw(G_result, with_labels=True)
        #nx.draw_networkx_edge_labels(G_result,font_size=8,edge_labels=edge_labels)
        DisplayDistance(matrix)
        plt.show()
        


def DisplayDistance(matrix):
    plt.figure(figsize=(5,5), dpi=90)# Control the windows dimensions
    plt.axis([0, 20, 0, 90])  
    for k in range(0,matrix.shape(0)): 
        #Browse all lines
        id = k
        name=GiveDistance(matrice,k)
        message="distance :"
        plt.text(6, 90-k, id,fontsize=6)
        plt.text(8, 90-k, message,fontsize=6)
        plt.text(10, 90-k, name,fontsize=6)
    plt.axis('off') # Hide the axes
    plt.title("Distance between Gotham and the other town") # Write title


def GiveDistance(matrice,index):
    for k in range(0,matrix.shape(1)):
        if matrix[k][index] !=0:
            value= matrix[k][index] 
    return value




#-------------DEFINE VARIABLE-----------#

#Initialise the graph with the value given in the subject
GothamPath = Graph(10) 
GothamPath.graph = [[0, 8.1, 9.2, 7.7, 9.3, 2.3, 5.1, 10.2, 6.1, 7.0], 
                   [8.1, 0, 12, 0.9, 12, 9.5, 10.1, 12.8, 2, 1], 
                   [9.2, 12, 0, 11.2, 0.7, 11.1, 8.1, 1.1, 10.5,11.5], 
                   [7.7, 0.9, 11.2, 0, 11.2, 9.2, 9.5, 12, 1.6,1.1], 
                   [9.3, 12, 0.7, 11.2, 0, 11.2, 8.5, 1, 10.6,11.6], 
                   [2.3, 9.5, 11.1, 9.2, 11.2, 0, 5.6, 12.1, 7.7,8.5], 
                   [5.1, 10.1, 8.1, 9.5, 8.5, 5.6, 0, 9.1, 8.3, 9.3], 
                   [10.2, 12.8, 1.1, 12, 1, 12.1, 9.1, 0, 11.4,12.4], 
                   [6.1, 2, 10.5, 1.6, 10.6, 7.7, 8.3, 11.4, 0,1.1],
                   [7, 1, 11.5, 1.1, 11.6, 8.5, 9.3, 12.4, 1.1, 0] 
                   ]; 



# ----------------------------------------------------------------- MAIN ------------------------------------------------------

def main():
    # Launch Dijkstra algorithm on the GothamPath graph
    GothamPath.Dijkstra(0); #(start=0 to take the fisrt line/column as start point for the algorithm)

if __name__ == "__main__":
    main()



  