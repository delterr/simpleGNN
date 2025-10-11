from tree import Node
from GNN import GNN
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

if __name__ == "__main__":

    T = Node("A")
    T.children = [Node("B")]
    case_functions = [case1, case2, case3, case4, case5, case6, case7, case8]

    G, A = case8()
    homs = total_hom(A, G)

    print(homs)

    # nx.draw(G.g_disp, labels=label_dict, node_color=color_map, with_labels=True, font_weight='bold') drawes labels and colours