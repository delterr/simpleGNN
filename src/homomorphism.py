from graph import Graph
from tree import Node

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

def create_tree():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")

    A.children = [B, C]
    B.children = [D, E]
    C.children = [F, G]
    
    return A

def create_graph():
    G = Graph(node_values=[(1,), (1,), (1,), (1,), (1,), (1,), (1,)], directed=False)

    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(1, 5)
    G.add_edge(1, 6)
    
    return G

if __name__ == "__main__":
    T = Node("A")
    T.children = [Node("B")]
    G = create_graph()
    for i in range(G.num_nodes):
        res = hom(T, G, i)
        print(f"{i}: {res}")
                