import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

A = np.matrix([ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]])

G = nx.from_numpy_matrix(A)

pos=nx.spring_layout(G)

nx.draw(G,pos,with_labels=True)

nx.draw_networkx_edge_labels(G,pos)

#BLABLABLA
plt.show()