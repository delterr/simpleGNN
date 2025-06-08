from activations import sigmoid

import math
import random

class Graph:
    def __init__(self, num_nodes, node_values=None):
        self.num_nodes = num_nodes
        self.node_values = node_values
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i == j:
                    self.adj_matrix[i][j] = "X"
    
    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
    
    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0
    
    def __repr__(self):
        final_string = ""
        row_string = "   " + " ".join([str(i) for i in range(self.num_nodes)])
        print(row_string)
        print("=" * len(row_string))
        
        for i, row in enumerate(self.adj_matrix):
            final_string += str(i) + "| "
            for k in row:
                final_string += str(k) + " "
            
            if i != len(self.adj_matrix) - 1:
                final_string += "\n"
                
        return final_string    
        
class GNN(Graph):
    def __init__(self, num_nodes, node_values):
        super().__init__(num_nodes, node_values)
        self.target_nodes = [node for node in range(num_nodes)]
    
    def add_edge(self, u, v):
        super().add_edge(u, v)
    
    def remove_edge(self, u, v):
        super().remove_edge(u, v)
    
    def transform(self, x):
        return random.random() * x + (random.random() / 10) # arbitrary affine transformation
    
    def aggregate(self, node):
        aggregated_value = 0
        
        for i, row in enumerate(self.adj_matrix):
            if isinstance(row[node], int):
                aggregated_value += self.transform(self.node_values[i])
        
        return aggregated_value

    def update(self):
        for node in self.target_nodes:
            aggr_value = self.aggregate(node)
            new_val = sigmoid(self.transform(self.node_values[node]) + aggr_value)
            self.node_values[node] = new_val
        
        return self.node_values
        
    def __repr__(self):
        return super().__repr__()

G = GNN(num_nodes=4, node_values=[random.random() for i in range(4)])

G.add_edge(0, 3)
G.add_edge(1, 3)
G.add_edge(2, 3)

print(G)
print("=" * 20)
print(G.node_values)
for i in range(10000):
    G.update()
print("=" * 20)
print(G.node_values)
