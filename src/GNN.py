from graph import Graph

import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class GNN(Graph):
    def __init__(self, node_values):
        super().__init__(node_values)
        self.target_nodes = [node for node in range(self.num_nodes)] # Node IDs e.g [0 1 2 3 4 ...]
        
    def add_edge(self, u, v):
        super().add_edge(u, v)
    
    def remove_edge(self, u, v):
        super().remove_edge(u, v)
    
    def transform(self, node):
        pass
    
    def update(self):
        temp_node_values = self.node_values[:] # make a copy
        for i, row in enumerate(self.adj_matrix):
            for j, val in enumerate(row):
                if val == 1:
                    self.node_values[i] += temp_node_values[j]
            self.node_values[i] -= 1
                    
        return self.node_values
            
    def __repr__(self):
        return super().__repr__()

G = GNN(node_values=[1, 1, 1, 1, 1, 1, 1])

G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(1, 5)
G.add_edge(1, 6)

if __name__ == "__main__":
    print(G)
    print("=" * 20)
    print(G.node_values)
    for i in range(1):
        A = G.update()
        print(A)
    print("=" * 20)
    
    color_map = []
    for node in G.node_values:
        if node == 1:
            color_map.append('blue')
        elif node == 2:
            color_map.append('green')
        elif node == 3:
            color_map.append('red')
        else:
            color_map.append('gray')
    
    label_dict = {}
    
    for i in range(len(G.node_values)):
        label_dict[i] = G.node_values[i]
    
    nx.draw(G.g_disp, node_color=color_map, labels=label_dict, with_labels=True, font_weight='bold')

    plt.show()
            
