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

    def is_left_child(self):
        """Return True if node is left child"""
        return self.parent and self.parent.left == self

    def get_left_child(self):
        """Return the left child node of this node."""
        return self.left

    def is_right_child(self):
        """Return True if node is right child"""
        return self.parent and self.parent.right == self

    def get_right_child(self):
        """Return the right child node of this node."""
        return self.right

    def has_child(self):
        return (self.left | self.right)

    def get_height(self):
        """Return the height of this node."""
        return self.height

    def update_height(self):
        """Update the height based on the height of the left and right nodes."""
        # self.height = 1 + max(self.left.height, self.right.height)

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

    def __str__(self):
        """Returns the string representation of the node in format: 'key/value'.
           If no value is stored, the representation is just: 'key'."""
        if not self.value:
            return "{0}".format(self.key)
        else:
            return "{0}/{1}".format(self.key, self.value)
