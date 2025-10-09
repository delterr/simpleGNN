import networkx as nx

petersen_edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
        (5, 6), (6, 7), (7, 8), (8, 9), (9, 5),
        (0, 5), (1, 8), (2, 6), (4, 7), (3, 9)
]

class Graph:
    def __init__(self, edges, directed=False):
        self.seen_nodes = []
        self.transform_edges(edges)
        self.num_nodes = len(self.seen_nodes)
        self.directed = directed
        self.adj_list = {node: [] for node in self.seen_nodes}
        self.setup_display()
        self.unpack_edges(edges)
        self.node_values = {node: (1,) for node in self.seen_nodes}

    def add_edge(self, u, v):
        if v in self.adj_list[u]:
            return "edge already exists"
        
        if u in self.adj_list[v]:
            return "edge already exists"

        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.g_disp.add_edge(u, v)
    
    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)
    
    def unpack_edges(self, edges):
        for edge in edges:
            self.add_edge(*edge)
    
    def setup_display(self):
        if self.directed:
            self.g_disp = nx.DiGraph()
        else:
            self.g_disp = nx.Graph()
    
    def transform_edges(self, edges):
        for edge in edges:
            if edge[0] not in self.seen_nodes:
                self.seen_nodes.append(edge[0])
            if edge[1] not in self.seen_nodes:
                self.seen_nodes.append(edge[1])
    
    def __repr__(self):
        final_string = ""
        for i in self.adj_list:
            final_string += f"{i}: {self.adj_list[i]}\n"
        
        return final_string
