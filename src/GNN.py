from activations import sigmoid
from graph import Graph

import math
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class GNN(Graph):
    def __init__(self, node_values):
        super().__init__(node_values)
        self.target_nodes = [node for node in range(self.num_nodes)]
        self.weight_matrix = np.random.rand(node_values.shape[0], node_values.shape[1])  # Random weight matrix for the node values
    
    def add_edge(self, u, v):
        super().add_edge(u, v)
    
    def remove_edge(self, u, v):
        super().remove_edge(u, v)
    
    def transform(self, x, i):
        return self.weight_matrix[i] * x
    
    def aggregate(self, node):
        aggregated_value = np.zeros((1, 3), dtype=np.float64)  # Initialize with zero vector
        
        for i, row in enumerate(self.adj_matrix):
            if isinstance(row[node], int):
                aggregated_value += self.transform(self.node_values[i], i)
        
        return aggregated_value

    def update(self):
        for i, node in enumerate(self.target_nodes):
            aggr_value = self.aggregate(node)
            new_val = sigmoid(self.transform(self.node_values[node], i) + aggr_value)
            self.node_values[node] = new_val
                    
        return self.node_values
        
    def __repr__(self):
        return super().__repr__()

G = GNN(node_values=np.array([[2, 3, 4], [6, 8, 10], [12, 14, 16], [18, 20, 22]], dtype=np.float64))

G.add_edge(0, 3)
G.add_edge(1, 3)
G.add_edge(2, 3)

if __name__ == "__main__":
    print(G)
    print(G.weight_matrix)
    print(G.weight_matrix.shape)
    print(G.node_values.shape)
    print("=" * 20)
    print(G.node_values)
    for i in range(4):
        G.update()
        print(G.node_values)
    print("=" * 20)
    
    subax1 = plt.subplot(121)
    nx.draw(G.g_disp, with_labels=True, font_weight='bold')
    subax2 = plt.subplot(122)
    nx.draw_shell(G.g_disp, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

    plt.show()
            
