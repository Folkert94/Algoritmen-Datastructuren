from node import Node

class BST(object):
    def __init__(self, key_list=[]):
        """Create a new BST, set its attributes, and insert all the keys in
           the key_list into the BST."""
        self.root = None
        for i in range(len(key_list)):
            self.insert(key_list[i])


    def get_root(self):
        """Return the root of the BST."""
        return self.root

    def is_empty(self):
        """Return True if the BST is empty."""
        if self.root == None:
            return True

    def find_max(self):
        """Return the node with the maximum key in the BST."""
        pass

    def find_min(self):
        """Return the node with the minimum key in the BST."""
        pass

    def search(self, key):
        """Return the Node object containing the key if the key exists in
           the BST, else return None."""
        pass

    def contains(self, key):
        """ Return True if the key exists in the BST, else return False."""
        pass

    def insert(self, key, value=None):
        """Create a new node for this key and value, and insert it into the BST.

           Return the new inserted node, or None if the key and value could not
           be inserted."""
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = Node(key, value)
            self.root.height = 0

    def _insert(self, key, value, node):
        """Recursive function for insert"""
        if key < node.key:
            if node.get_left_child():
                self._insert(key, value, node.left)
            else:
                node.left = Node(key, value)
                node.left.parent = node
                node.update_height()
        else:
            if node.get_right_child():
                self._insert(key, value, node.right)
            else:
                node.right = Node(key, value)
                node.right.parent = node
                node.update_height()

    def delete(self, key):
        """Remove the Node object containing the key if the key exists in
           the BST and return the removed node, else return None.

           The returned node is the actual Node object that got removed
           from the BST, and so might be successor of the removed key."""
        pass

    def in_order_traversal(self):
        """Return a list of the Nodes in the tree in sorted order."""
        pass

    def breadth_first_traversal(self):
        """Return a list of lists, where each inner lists contains the elements
           of one layer in the tree. Layers are filled in breadth-first-order,
           and contain contain all elements linked in the BST, including the
           None elements.
           >> BST([5, 8]).breadth_first_traversal()
           [[Node(5)], [None, Node(8)], [None, None]]"""
        pass

    def __str__(self):
        """Return a string containing the elements of the tree in breadth-first
           order, with each on a new line, and None elements as `_`, and
           finally a single line containing all the nodes in sorted order.
           >> print(BST([5, 8, 3]))
           5
           3 8
           _ _ _ _
           3 5 8
           """
        pass
