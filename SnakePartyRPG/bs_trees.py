
class Node:
    """ Node implementation for BST. """

    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    def __repr__(self):
        return str(self.val)


class BSTree:
    """ Classic binary search tree. """

    def __init__(self):
        self.root = None

    def __repr__(self):
        self.sorted = []
        self.get_pre_order(self.root)
        return str(self.sorted)

    def get_pre_order(self, node):
        """ Traverse leaves of tree: node, left, right. """
        if node:
            self.sorted.append(str(node.val))
            self.get_pre_order(node.left)
            self.get_pre_order(node.right)

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val <= node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val)
