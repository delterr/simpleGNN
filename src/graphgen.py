"""
Generates random graphs

Can either generate a random d-degree regular graph with n-vertices or a fully connected
n -> n bipartite graph
"""

import sys
import pickle
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

def arg_check(n_args, error):
    """Check if number of arguments is correct"""
    if len(sys.argv) != n_args:
        raise Exception(error)

def save_graph():
    mode = sys.argv[1]

    if mode == "bip":
        nodes = int(sys.argv[2])

        filename = f"../graphs/bipartite/bip_{nodes}.pkl"

        graph, edges = generate_bipartite(nodes)


    elif mode == "reg":
        degree = int(sys.argv[2])
        nodes = int(sys.argv[3])

        filename = f"../graphs/regular/reg_{degree}_{nodes}.pkl"

        graph, edges = generate_regular(degree, nodes)

    else:
        raise Exception(f"Invalid Mode: {mode}")


    with open(filename, "wb") as f:
        pickle.dump(edges, f)

    print("Graph Successfully Created!")
    
save_graph()
