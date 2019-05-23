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

    @staticmethod
    def get_node(char):
        new_node = Node()
        new_node.char = char
        return new_node

    def insert(self, node, key):
        if len(key) == 0:
            node.mid = self.get_node(None)
            node.mid.is_end = True
            return node

        head = key[0]
        tail = key[1:]

        if node.char is None:
            node.char = head
            self.insert(node, tail)
        elif head < node.char and node.mid is not None:
            if node.left is not None:
                self.insert(node.left, key)
            else:
                node.left = self.get_node(head)
                self.insert(node.left, tail)
        elif head > node.char and node.mid is not None:
            if node.right is not None:
                self.insert(node.right, key)
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

    def search(self, node: list or Node, key: str):
        if len(key) == 0:
            if node.is_end:
                return True
            else:
                return False
        elif node.char is None or node is None:
            return False

        head = key[0]
        tail = key[1:]

        if node.char == head:
            return self.search(node.mid, tail)
        elif head < node.char and node.left is not None:
            return self.search(node.left, key)
        elif head > node.char and node.right is not None:
            return self.search(node.right, key)
        else:
            return False

    def to_string(self, node):
        tree_nodes = {}
        for k, v in node.__dict__.items():
            tree_nodes[k] = v
            tree_nodes[k] = v
            if isinstance(v, Node):
                tree_nodes[k] = self.to_string(v)
        return tree_nodes

    #### TO_DO ####
    # - Import/export tree to json
    # - Delete


tree = TernTree()
root = Node()
tree_list = ['eric', 'mike', 'able', 'aria', 'bri', 'abby', 'erica', 'erin']
search_list = ['jared', 'eric', 'ariana', 'aria', 'arias', 'able', 'ericah', 'erin']

for i in tree_list:
    tree.insert(root, i)

for i in search_list:
    if tree.search(tree.root_node, i):
        print('true')
    elif not tree.search(tree.root_node, i):
        print('false')
