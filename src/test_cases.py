import os
import pickle
from pathlib import Path

from GNN import GNN
from tree import Node
from homomorphism import total_hom

petersen_edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
        (5, 6), (6, 7), (7, 8), (8, 9), (9, 5),
        (0, 5), (1, 8), (2, 6), (4, 7), (3, 9)
]

def case1():
    """
    Example 1
    """
    edges = [(0, 1), (0, 2)]

    G = GNN(edges=edges, directed=False)


    A = Node("A")
    B = Node("B")

    A.children = [B]

    return G, A

def case2():
    """
    Example 2
    """

    edges = [(0, 1), (0, 2), (2, 3), (3, 1), (3, 0), (2, 1)]

    G = GNN(edges=edges, directed=False)

    A = Node("A")
    B = Node("B")

    A.children = [B]

    return G, A


def case3():
    """
    Example 3
    """

    edges = [(0, 1), (0, 2), (2, 3), (3, 1)]

    G = GNN(edges=edges, directed=False)

    A = Node("A")
    B = Node("B")

    A.children = [B]

    return G, A

def case4():
    """
    Example 5
    """
    G = GNN(edges=petersen_edges, directed=False)    

    A = Node("A")
    B = Node("B")

    A.children = [B]

    return G, A

def case5():
    """
    Example 5
    """
    edges = [(0, 1), (0, 2)]

    G = GNN(edges=edges, directed=False)

    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.children = [B, C]

    return G, A

def case6():
    """
    Example 6
    """

    edges = [(0, 1), (0, 2), (2, 3), (3, 1), (0, 3), (1, 2)]

    G = GNN(edges=edges, directed=False)

    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.children = [B, C]

    return G, A

def case7():
    """
    Example 7
    """
    edges = [(0, 1), (0, 2), (2, 3), (3, 1)]

    G = GNN(edges=edges, directed=False)

    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.children = [B, C]

    return G, A

def case8():
    """
    Example 8
    """
    G = GNN(edges=petersen_edges, directed=False)

    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.children = [B, C]

    return G, A

def regular_tests():
    """
    Count number of homomorphisms on regular graphs

    Compare this value to the number of homormorphisms from GNN

    Computes n * d^(k - 1)
    """

    cases = [
            (5, 10), (5, 100), (5, 150), (5, 200), 
            (10, 20), (10, 100), (10, 150), (10, 200),
            (20, 30), (30, 40), (40, 50), (50, 100),
            (150, 200), (200, 250)
        ] # regular graph cases of degree d and number of nodes n (d, n)

    tree1 = Node("A")
    tree1.children = [Node("B")]
    k1 = 2
    
    tree2 = Node("A")
    tree2.children = [Node("B"), Node("C")]
    k2 = 3

    tree_sizes = [k1, k2] # sizes of trees

    # final homomorphism counts for k1 and k2
    k1_homs = []
    k2_homs = [] 

    for case in cases:
        k1_homs.append(case[1] * case[0] ** (tree_sizes[0] - 1))
        k2_homs.append(case[1] * case[0] ** (tree_sizes[1] - 1))

    k1_homs_gnn = []
    k2_homs_gnn = []

    path = "../graphs/regular/"

    for filename in os.listdir(path):
        with open(f"{path}/{filename}", "rb") as f:
            edges = pickle.load(f)

        G = GNN(edges=edges, directed=False)
        k1_homs_gnn.append(total_hom(tree1, G))
        k2_homs_gnn.append(total_hom(tree2, G))
    
    comp1 = k1_homs == k1_homs_gnn
    comp2 = k2_homs == k2_homs_gnn
            
    
    return comp1, comp2

def bipartite_tests():
    pass

if __name__ == "__main__":

    T = Node("A")
    T.children = [Node("B")]
    case_functions = [case1, case2, case3, case4, case5, case6, case7, case8]

    """
    for func in case_functions:
        G, A = func()
        homs = total_hom(A, G)

        print(homs)
    """

    print(regular_tests()[0])
    print(regular_tests()[1])


    # nx.draw(G.g_disp, labels=label_dict, node_color=color_map, with_labels=True, font_weight='bold') drawes labels and colours
 