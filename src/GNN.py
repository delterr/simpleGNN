from graph import Graph

class GNN(Graph):
    def __init__(self, edges, directed=False):
        super().__init__(edges, directed)

    def add_edge(self, u, v):
        super().add_edge(u, v)
    
    def remove_edge(self, u, v):
        super().remove_edge(u, v)
    
    def unpack_edges(self, edges):
        super().unpack_edges(edges)
    
    def update(self):
        temp_node_values = self.node_values.copy() # make a copy

        for i in self.adj_list:
            for j in self.adj_list[i]:
                self.node_values[i] = self.node_values[i] + temp_node_values[j]
        
        self.node_values = {i: hash(self.node_values[i]) for i in self.node_values}  # Hashing the node values
        return self.node_values
            
    def __repr__(self):
        return super().__repr__()

def partition(colour_array):
    colours = {i: [] for i in colour_array}
    for key1, value1 in colour_array.items():
        for key2, value2 in colour_array.items():
            if value1 == value2:
                colours[key1].append(key2)
    return colours
