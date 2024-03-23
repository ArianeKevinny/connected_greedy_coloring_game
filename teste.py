class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, target):
        target.children = [child for child in target.children if child.data != target.data]
        for child in target.children:
            child.remove_child(target)

def print_tree(root, level=0):
    if root is None:
        return
    print("  " * level + str(root.data))
    for child in root.children:
        print_tree(child, level + 1)

# Exemplo de uso:
if __name__ == "__main__":
    # Criando a árvore
    root = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")

    root.add_child(b)
    root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)
    c.add_child(g)

    # Imprimindo a árvore antes de remover um nó
    print("Árvore antes de remover o nó 'D':")
    print_tree(root)

    # Removendo o nó 'D'
    root.remove_child(b)

    # Imprimindo a árvore após remover o nó 'D'
    print("\nÁrvore após remover o nó 'B':")
    print_tree(root)
