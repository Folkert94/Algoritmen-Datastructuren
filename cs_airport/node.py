class Node(object):
    def __init__(self, key, value=None):
        """Store the key and value in the node and set the other attributes."""
        self.left = None;
        self.right = None;
        self.parent = None;
        self.height = 0;
        self.key = key;
        self.value = value;

    def get_key(self):
        """Return the key of this node."""
        return self.key

    def get_value(self):
        """Return the value of this node."""
        return self.value

    def get_parent(self):
        """Return the parent node of this node."""
        return self.parent

    def get_left_child(self):
        """Return the left child node of this node."""
        return self.left

    def get_right_child(self):
        """Return the right child node of this node."""
        return self.right

    def get_height(self):
        """Return the height of this node."""
        return self.height

    def max_height(self):
        """Return max_height from children nodes"""
        if self.left and self.right:
            return max(self.left.height, self.right.height)
        elif self.left is not None and self.right is None:
            return self.left.height
        elif self.left is None and self.right is not None:
            return self.right.height
        else:
            return -1

    def update_height(self):
        """Update the height based on the height of the left and right nodes."""
        node = self
        while node is not None:
            node.height = node.max_height() + 1
            node = node.parent

    #
    # You can add any additional node functions you might need here
    #

    def __eq__(self, other):
        """Returns True if the node is equal the other node or value."""
        return self.key == other

    def __neq__(self, other):
        """Returns True if the node is not equal the other node or value."""
        return self.key != other

    def __lt__(self, other):
        """Returns True if the node is less than the other node or value."""
        return self.key < other

    def __le__(self, other):
        """Returns True if the node is less or equal to the other node or value."""
        return self.key <= other

    def __gt__(self, other):
        """Returns True if the node is greater than the other node or value."""
        return self.key > other

    def __ge__(self, other):
        """Returns True if the node is greater or equal to the other node or value."""
        return self.key >= other

    def is_left_child(self):
        """Return True if node is left child"""
        return self.parent and self.parent.left == self

    def is_right_child(self):
        """Return True if node is right child"""
        return self.parent and self.parent.right == self

    def has_child(self):
        """Return None if Node has no children or returns one of children"""
        return (self.left or self.right)

    def has_one_child(self):
        """Return True if Node has one child"""
        if self.left == None and self.right != None:
            return True
        if self.left != None and self.right == None:
            return True
        else:
            return False

    def next(self):
        """Return next node with larger value or None"""
        if self.right is not None:
            node = self.right
            while node.left is not None:
                node = node.left
            return node

        node = self
        while node.parent is not None:
            if node.parent.left == node:
                return node.parent
            node = node.parent

        return None

    def get_children(self):
        "Returns children nodes"
        return self.get_left_child(), self.get_right_child()

    def weight(self):
        """Weighs children nodes and returns weight"""
        if self.has_child() == None:
            return 0
        if self.has_one_child():
            if self.right != None:
                return self.height
            if self.left != None:
                return - self.height
        else:
            return self.right.height - self.left.height

    def swap_nodes(self, advance, temp):
        """Swap parent nodes and return the new top node"""
        advance.parent = self.parent
        self.parent = advance
        if temp is not None:
            temp.parent = self

        if advance.parent is not None:
            if advance.parent.right == self:
                advance.parent.right = advance
            if advance.parent.left == self:
                advance.parent.left = advance
        return advance

    def __str__(self):
        """Returns the string representation of the node in format: 'key/value'.
           If no value is stored, the representation is just: 'key'."""
        if not self.value:
            return "{0}".format(self.key)
        else:
            return "{0}/{1}".format(self.key, self.value)

    def __repr__(self):
        return "Node({0})".format(self.key)
