import networkx as nx

class Graph:
    def __init__(self, edges, directed=False):
        self.seen_nodes = []
        self.transform_edges(edges)
        self.num_nodes = len(self.seen_nodes)
        self.node_values = [(1,) for i in range(self.num_nodes)]
        self.directed = directed
        self.adj_matrix = [[0] * self.num_nodes for _ in range(self.num_nodes)]
        self.setup_display()
        self.unpack_edges(edges)

    def add_edge(self, u, v):
        if self.directed:
            self.adj_matrix[u][v] = "X"
        else:
            self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        self.g_disp.add_edge(u, v)
    
    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0
    
    def unpack_edges(self, edges):
        for edge in edges:
            self.add_edge(*edge)
    
    def setup_display(self):
        if self.directed:
            self.g_disp = nx.DiGraph()
        else:
            self.g_disp = nx.Graph()
        
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if i == j:
                    self.adj_matrix[i][j] = "X"
    
    def transform_edges(self, edges):
        for edge in edges:
            if edge[0] not in self.seen_nodes:
                self.seen_nodes.append(edge[0])
            if edge[1] not in self.seen_nodes:
                self.seen_nodes.append(edge[1])
    
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
