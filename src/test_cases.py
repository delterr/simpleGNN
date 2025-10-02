from tree import Node
from GNN import GNN
import matplotlib.pyplot as plt
from matplotlib import colors
from homomorphism import total_hom
import networkx as nx


petersen_edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
        (5, 6), (6, 7), (7, 8), (8, 9), (9, 5),
        (0, 5), (1, 8), (2, 6), (4, 7), (3, 9)
]

def unpack_edges(G, edges):
    for edge in edges:
        G.add_edge(*edge)

def case1():
    """
    Example 1
    """
    G = GNN(node_values=[(1,), (1,), (1,)], directed=False)

    edges = [(0, 1), (0, 2)]

    unpack_edges(G, edges)

    A = Node("A")
    B = Node("B")

    A.children = [B]

    return G, A

def case2():
    """
    Example 2
    """
    G = GNN(node_values=[(1,), (1,), (1,), (1,)], directed=False)

    edges = [(0, 1), (0, 2), (2, 3), (3, 1), (3, 0), (2, 1)]

    unpack_edges(G, edges)

    A = Node("A")
    B = Node("B")

    A.children = [B]

    return G, A


def case3():
    """
    Example 3
    """
    G = GNN(node_values=[(1,), (1,), (1,), (1,)], directed=False)

    edges = [(0, 1), (0, 2), (2, 3), (3, 1)]

    unpack_edges(G, edges)

    A = Node("A")
    B = Node("B")

    A.children = [B]

    return G, A

def case4():
    """
    Example 5
    """
    G = GNN(node_values=[(1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,)], directed=False)

    edges = petersen_edges
    
    unpack_edges(G, edges)
    

    A = Node("A")
    B = Node("B")

    A.children = [B]

    return G, A

def case5():
    """
    Example 5
    """
    G = GNN(node_values=[(1,), (1,), (1,)], directed=False)

    edges = [(0, 1), (0, 2)]

    unpack_edges(G, edges)

    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.children = [B, C]

    return G, A

def case6():
    """
    Example 6
    """
    G = GNN(node_values=[(1,), (1,), (1,), (1,)], directed=False)

    edges = [(0, 1), (0, 2), (2, 3), (3, 1), (0, 3), (1, 2)]

    unpack_edges(G, edges)

    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.children = [B, C]

    return G, A

def case7():
    """
    Example 7
    """
    G = GNN(node_values=[(1,), (1,), (1,), (1,)], directed=False)

    edges = [(0, 1), (0, 2), (2, 3), (3, 1)]

    unpack_edges(G, edges)

    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.children = [B, C]

    return G, A

def case8():
    """
    Example 8
    """
    G = GNN(node_values=[(1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,)], directed=False)

    edges = petersen_edges
    
    unpack_edges(G, edges)

    A = Node("A")
    B = Node("B")
    C = Node("C")

    A.children = [B, C]

    return G, A



if __name__ == "__main__":

    T = Node("A")
    T.children = [Node("B")]
    case_functions = [case1, case2, case3, case4, case5, case6, case7, case8]

    fig, axes = plt.subplots(4, 2, figsize=(10, 10))
    axes = axes.flatten()


    for index, func in enumerate(case_functions):
        colors = [
            "black",
            "red",
            "blue",
            "green",
            "orange",
            "purple",
            "brown",
            "pink",
            "gray",
            "cyan",
        ]

        G, A = func()
        homs = total_hom(A, G)
        print(f"Total homomorphisms for {func.__name__}: {homs}")

        color_map = []
        label_dict = {}
        colors_dict = {}

        print(homs)
        print(G.node_values)
        for i in range(len(G.node_values)):
            label_dict[i] = G.node_values[i]
            current_hash = G.node_values[i]

            if current_hash not in colors_dict:
                colors_dict[current_hash] = colors.pop(0)
        
        for node in G.node_values:
            color_map.append(colors_dict[node])
        
        nx.draw(G.g_disp, ax=axes[index], node_color=color_map)
        axes[index].set_title(f"Graph {index+1} \n #Homomorphisms: {homs}")

        print(colors_dict)
        print(color_map)
    
    # nx.draw(G.g_disp, labels=label_dict, node_color=color_map, with_labels=True, font_weight='bold') drawes labels and colours



    plt.show()

