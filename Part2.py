import sys

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source (vertex 1)")
        for node in range(self.V): 
            print (node+1, "\t", dist[node] )
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxsize 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist) 
  
# Driver program 
g = Graph(10) 
g.graph = [[0, 8.1, 9.2, 7.7, 9.3, 2.3, 5.1, 10.2, 6.1, 7.0], 
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
  
g.dijkstra(0); 
  