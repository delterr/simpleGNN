import pandas as pd
from GNN import GNN
from graph import Graph
import matplotlib.pyplot as plt
import networkx as nx
from homomorphism import total_hom
from tree import Node

df = pd.read_csv('../facebook/0.edges', sep=' ', header=None)

petersen_edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
        (5, 6), (6, 7), (7, 8), (8, 9), (9, 5),
        (0, 5), (1, 8), (2, 6), (4, 7), (3, 9)
]

def create_graph(df):
    edges = [(int(row[0]), int(row[1])) for index, row in df.iterrows()]
    G = GNN(edges=edges, directed=False)
    return G

G = create_graph(df)
A = Node("A")
B = Node("B")
C = Node("C")
A.children = [B, C]
B.children = [Node("D"), Node("E")]
C.children = [Node("F"), Node("G")]

total_homs = total_hom(A, G)
print(total_homs)
pos = nx.spring_layout(G.g_disp, k=1, iterations=100)

# Draw the graph
nx.draw(
    G.g_disp, pos,
)

plt.show()
