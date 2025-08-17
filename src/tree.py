class Node:
    def __init__(self, val):
        self.value = val
        self.children = []
    
        
    def __repr__(self):
        return f"Node({self.value})"

if __name__ == "__main__":
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


