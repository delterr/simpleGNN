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
        
        for y in G.adj_list.get(x): # iterate through keys
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
    
        print(colours)

    colour_count = Counter(A.values())
    print(colour_count)
    print(A)
    result = 0

    for key1, value1 in colour_count.items():
        for key2, value2 in A.items():
            if key1 == value2:
                node = key2
        result += value1 * hom(T, G, node)
    
    return result
