"""
Generates random graphs

Can either generate a random d-degree regular graph with n-vertices or a fully connected
n -> n bipartite graph
"""

import sys
import networkx as nx
import matplotlib.pyplot as plt

def generate_regular(degree, nodes):
    """Generate random d-regular graph with n-vertices"""
    graph = nx.random_regular_graph(degree, nodes)
    edges = list(graph.edges)

    return graph, edges

def generate_bipartite(n):
    "Generates a full n -> n bipartite graph"
    graph = nx.complete_bipartite_graph(n, n)
    edges = list(graph.edges)

    return graph, edges

degree = int(sys.argv[1])

try:
    nodes = int(sys.argv[2])
except IndexError:
    n = degree
    graph, edges = generate_bipartite(n)
else:
    graph, edges = generate_regular(degree, nodes)

print(edges)

nx.draw(graph)
plt.show()
