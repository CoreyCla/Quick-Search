class Node:
    def __init__(self):
        self.char = None
        self.children = []
        self.is_end = False
        self.child_chars = []


class TrieTree:
    def __init__(self):
        self.root_node =  None

    @staticmethod
    def get_node(char):
        new_node = Node()
        new_node.char = char
        return new_node

    def insert(self, key, node):
        if len(key) == 0:
            node.is_end = True
            return node

        head = key[0]
        tail = key[1:]

        if node.char is None and head not in node.child_chars:
            new_node = self.get_node(head)
            node.children.append(new_node)
            node.child_chars.append(head)
            self.insert(tail, new_node)
        elif head in node.child_chars:
            for child in node.children:
                if child.char == head:
                    self.insert(tail, child)
                    break
        else:
            new_node = self.get_node(head)
            node.child_chars.append(head)
            node.children.append(new_node)
            self.insert(tail, new_node)

        self.root_node = node

    def search(self, key, node=None):
        if len(key) == 0:
            if node.is_end:
                return True
            else:
                return False

        head = key[0]
        tail = key[1:]

        if node is None:
            node = self.root_node
            return self.search(key, node)
        else:
            if head in node.child_chars:
                for child in node.children:
                    if child.char == head:
                        return self.search(tail, child)
            else:
                return False

    # This method is only necessary if the data was not input alphabetically to begin with.
    def sort_tree(self, node=None):
        if node is None:
            self.sort_tree(self.root_node)
        elif len(node.children) > 1:
            sorted(node.children, key=lambda x: x.char)
            node.child_chars.sort()
            for child in node.children:
                self.sort_tree(child)

