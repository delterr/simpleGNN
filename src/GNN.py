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
        temp_node_values = self.node_values[:] # make a copy

        for i in self.adj_list:
            for j in self.adj_list[i]:
                self.node_values[i] = self.node_values[i] + temp_node_values[j]
        
        self.node_values = [hash(i) for i in self.node_values]  # Hashing the node values
        return self.node_values

    def update_list(self):
        temp_node_values = self.node_values[:]
        for i in self.adj_list:
            for j in self.adj_list[i]:
                self.node_values[i] = self.node_values[i] + temp_node_values[j]
        self.node_values = [hash(i) for i in self.node_values]
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
