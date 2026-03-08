class Node:
    def __init__(self, val):
        self.value = val
        self.children = []

    def __eq__(self, node):
        if not isinstance(node, Node):
            return NotImplemented
        return self.value == node.value

    def __repr__(self):
        return f"Node({self.value})"

class Tree:
    def __init__(self, edges):
        self.edges = edges
        self.nodes = {}

        self.edges = self.build_tree()
    
    def build_tree(self):
        for parent, child in self.edges:
            if parent not in self.nodes:
                self.nodes[parent] = Node(parent)
            
            if child not in self.nodes:
                self.nodes[child] = Node(child)
            
            self.nodes[parent].children.append(self.nodes[child])

        return self.edges

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
