from bst import BST

class AVL(BST):
    def __init__(self, key_list=[]):
        """Create a new AVL Tree, set its attributes, and insert all the keys in
           the key_list into the AVL."""
        BST.__init__(self, key_list)


    def insert(self, key, value=None):
        """Create a new node for this key and value, and insert it into the AVL
           using the BST insert operation. In addition, it ensures that the AVL
           tree is still balanced after this operation is performed.

           Return the new inserted node, or None if the key and value could not
           be inserted."""
        node = BST.insert(self, key, value=None)
        if node is None:
            return None

        self.fix_balance(node)
        return node

    def delete(self, key):
        """Remove the Node object containing the key if the key exists in
           the AVL using the BST delete operation. In addition, it ensures that
           the AVL tree is still balanced after this operation is performed.

           Return the node that actually got removed from the AVL, which might
           be successor of the removed key."""
        node = BST.delete(self, key)
        if node is None:
            return None

        self.fix_balance(node)
        if self.get_root().weight() > 1:
            self.fix_balance(self.find_max())
        if self.get_root().weight() < -1:
            self.fix_balance(self.find_min())

        return node

    @staticmethod
    def left_rotate(node):
        """Performs a right rotation of the specified node."""
        node1 = node.right
        node2 = node1.left
        node.right = node2
        node1.left = node
        new_par = node.swap_nodes(node1, node2)

        if node2 is not None:
            node2.update_height()
        node.update_height()

        return new_par

    @staticmethod
    def right_rotate(node):
        """Performs a left rotation of the specified node."""
        node1 = node.left
        node2 = node1.right

        node.left = node2
        node1.right = node

        new_par = node.swap_nodes(node1, node2)

        if node2 is not None:
            node2.update_height()
        node.update_height()

        return new_par

    def fix_balance(self, node):
        """Performs a sequence of rotations to fix the balance of a node and
           all its parent nodes if needed to maintain the AVL property."""
        while node.parent != None and node.parent.parent != None:

            if node.parent.parent.weight() < -1 and node.parent.weight() < 0:
                new_top = self.right_rotate(node.parent.parent)
                if new_top.parent is None:
                    self.root = new_top

            elif node.parent.parent.weight() > 1 and node.parent.weight() > 0:
                new_top = self.left_rotate(node.parent.parent)
                if new_top.parent is None:
                    self.root = new_top

            elif node.parent.parent.weight() < -1 and node.parent.weight() > 0:
                temp = self.left_rotate(node.parent)
                new_top = self.right_rotate(temp.parent)
                if new_top.parent is None:
                    self.root = new_top

            elif node.parent.parent.weight() > 1 and node.parent.weight() < 0:
                temp = self.right_rotate(node.parent)
                new_top = self.left_rotate(temp.parent)
                if new_top.parent is None:
                    self.root = new_top

            else:
                node = node.parent
