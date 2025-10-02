from GNN import partition
from collections import Counter

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
