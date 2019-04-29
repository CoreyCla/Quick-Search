class Node:
    def __init__(self):
        self.char = None
        self.left = None
        self.right = None
        self.mid = None
        self.is_end = False

    def to_string(self):
        print("Character: " + str(self.char),
              "Left: " + str(self.left),
              "Right: " + str(self.right),
              "Middle: " + str(self.mid),
              "Leaf Node: " + str(self.is_end))


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

    def insert(self, node, key):
        head = key[0]
        tail = key[1:]

        print(head)
        print(node.left)

        if len(key) == 0:
            return node

        # In the case of the root node being created and passed in
        if self.root_node is None:
            self.root_node = node
            self.root_node.char = head
            self.insert(node, tail)
        elif not tail:
            node.is_end = True
        elif head < node.char:
            node.left = self.insert(self.get_node(head), tail)
        elif head > node.char:
            node.right = self.insert(self.get_node(head), tail)
        else:
            node.mid = self.insert(self.get_node(head), tail)

    ########## TO-DO ##########
    def to_string(self, node):
        return None

    def search(self, node, key):
        return None


tree = TernTree()
root = Node()
tree_list = ['Mike', 'Maryanne', 'Jeff', 'Eric', 'Ericah', 'Michael']

for i in tree_list:
    tree.insert(root, i)
# print(tree.root_node)
# print(tree.root_node.to_string())
