from graph import Graph

import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

class GNN(Graph):
    def __init__(self, node_values, directed=False):
        super().__init__(node_values, directed)
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
                    self.node_values[i] = self.node_values[i] + temp_node_values[j]
        self.node_values = [hash(i) for i in self.node_values]  # Hashing the node values
        return self.node_values
            
    def __repr__(self):
        return super().__repr__()

def partition(colour_array):
    colours = {i: [] for i in range(len(colour_array))}
    for index1, colour1 in enumerate(colour_array):
        for index2, colour2 in enumerate(colour_array):
            if colour1 == colour2:
                colours[index1].append(index2)
    return colours

G = GNN(node_values=[(1,), (1,), (1,), (1,), (1,), (1,), (1,)], directed=False)

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
    
    prev_partition = {}
    same_partiton = False
    i = 0
    while not same_partiton:
        print(f"Iteration {i}")
        A = G.update()
        print(A)
        colours = partition(A)
        i += 1
        if colours == prev_partition:
            print(f"Colours successfully refined after {i} iterations.")
            same_partiton = True
        else:
            prev_partition = colours
    colour_count = Counter(A)
    print(colour_count)
    print("=" * 20)

    
    label_dict = {}
    
    for i in range(len(G.node_values)):
        label_dict[i] = G.node_values[i]
    
    nx.draw(G.g_disp, labels=label_dict, with_labels=True, font_weight='bold')

    plt.show()
            
