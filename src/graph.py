import networkx as nx

class Graph:
    def __init__(self, node_values=None):
        self.num_nodes = len(node_values) if node_values is not None else 0
        self.node_values = node_values
        self.adj_matrix = [[0] * self.num_nodes for _ in range(self.num_nodes)]
        self.g_disp = nx.Graph()
        
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if i == j:
                    self.adj_matrix[i][j] = "X"
    
    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        self.g_disp.add_edge(u, v)
    
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