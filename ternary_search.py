class Node:
    def __init__(self):
        self.char = None
        self.left = None
        self.right = None
        self.mid = None
        self.is_end = False


class TernTree:
    def __init__(self):
        self.root_node = None

    def __iter__(self):
        for attr, value in self.__dict__.items():
            return attr, value

    @staticmethod
    def get_node(char):
        new_node = Node()
        new_node.char = char
        return new_node

    def insert(self, node, string):
        if len(string) == 0:
            # self.root_node = node
            node.is_end = True
            return node

        head = string[0]
        tail = string[1:]

        if node.char is None:
            node.char = head
            self.insert(node, tail)
        elif head < node.char and node.mid is not None:
            if node.left is not None:
                self.insert(node.left, string)
            else:
                node.left = self.get_node(head)
                self.insert(node.left, tail)
        elif head > node.char and node.mid is not None:
            if node.right is not None:
                self.insert(node.right, string)
            else:
                node.right = self.get_node(head)
                self.insert(node.right, tail)
        else:
            if node.mid is not None and node.char == head:
                self.insert(node.mid, tail)
            else:
                node.mid = self.get_node(head)
                self.insert(node.mid, tail)

        self.root_node = node

    ########## TO-DO ##########
    def to_string(self, node):
        tree_nodes = {}
        for k, v in node.__dict__.items():
            tree_nodes[k] = v
            if isinstance(v, Node):
                tree_nodes[k] = self.to_string(v)
        return tree_nodes

    def search(self, node, key):
        return None


tree = TernTree()
root = Node()
tree_list = ['mike', 'jeff', 'eric', 'ericah']

for i in tree_list:
    tree.insert(root, i)
# print(tree.root_node)
# print(tree.root_node.to_string())
print(tree.to_string(tree.root_node))
