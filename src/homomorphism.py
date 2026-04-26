from GNN import partition
from collections import Counter


def refine_colours(G):
    """
    Refine colours on a graph G
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
    
    colour_count = Counter(A.values())

    return A, colour_count

def total_hom_preprocess(T, G, colour_count, A):
    memo = {}
    result = 0

    for key1, value1 in colour_count.items():
        for key2, value2 in A.items():
            if key1 == value2:
                node = key2
        result += value1 * hom(T, G, node, memo)
    
    
    return result

def hom(T, G, x, memo=None):
    if memo is None:
        memo = {}
    
    if not T.children:
        return 1
    
    result = 1
    
    for u in T.children:
        temp = 0
        for y in G.adj_list.get(x, []):
            key = (id(u), y)
            if key not in memo:
                memo[key] = hom(u, G, y, memo)
            temp += memo[key]
        result *= temp
    
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
    
    colour_count = Counter(A.values())
    result = 0

    for key1, value1 in colour_count.items():
        for key2, value2 in A.items():
            if key1 == value2:
                node = key2
        result += value1 * hom(T, G, node)
    
    return result
