from graph import Graph
from tree import Node
from GNN import GNN, partition
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx

def hom(T, G, x):
    """
    Compute homomorphism between tree T and graph G
    from a vertex v in T to a vertex x in G.
    """
    
    if len(T.children) == 0:
        return 1
    
    result = 1
    
    for u in T.children:
        T_prime = u
        temp = 0
        
        for y in range(G.num_nodes):
            if G.adj_matrix[x][y] == 1:
                temp += hom(T_prime, G, y)
        result = result * temp
    return result

def total_hom(T, G):
    """
    Compute total homomorphisms between tree T and graph G.
    """
    prev_partition = {}
    same_partiton = False
    i = 0
    while not same_partiton:
        A = G.update()
        colours = partition(A)
        i += 1
        if colours == prev_partition:
            same_partiton = True
        else:
            prev_partition = colours    

    colour_count = Counter(A)
    print(colour_count)
    result = 0
    i = 0
    for key, value in colour_count.items():
        i += 1
        node = A.index(key)
        result += value * hom(T, G, node)
    
    return result

def create_tree():
    A = Node("A")
    B = Node("B")

    A.children = [B]
    
    return A

def create_graph():
    G = GNN(node_values=[(1,), (1,), (1,)], directed=False)

    G.add_edge(0, 1)
    G.add_edge(0, 2)

    return G

if __name__ == "__main__":
    T = Node("A")
    T.children = [Node("B")]
    G = create_graph()

    label_dict = {}

    print(total_hom(T, G))

    for i in range(len(G.node_values)):
        label_dict[i] = G.node_values[i]
    
    nx.draw(G.g_disp, labels=label_dict, with_labels=True, font_weight='bold')

    plt.show()
