class Node:
    def __init__(self):
        self.children = []

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.get_node()

    @staticmethod
    def get_node():
        return Node()

    @staticmethod
    def _char_dec(ch):
        # Gets the unicode decimal value for
        return ord(ch) - ord(' ')

    def insert(self, key):
        a_node = self.root
        length = len(key)
        for level in range(length):
            index = self._char_dec(key[level])

            # if current character is not present
            if not a_node.children[index]:
                a_node.children[index] = self.get_node()
            a_node = a_node.children[index]

            # mark last node as leaf
        a_node.isEndOfWord = True

    def search_all(self, cols, key):
        a_node = self.root
        length = len(key)
        for level in range(length):
            # Extracts the character at the n node level in the key
            ch_index = key[level]
            # If the node
            if not a_node.children[ch_index]:
                return False
            a_node = a_node.children[ch_index]

        return a_node is not None and a_node.isEndOfWord
