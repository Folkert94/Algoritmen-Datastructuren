"""
Folkert Stijnman

10475206

Datastructuren & Algoritmen

Node class for the Binary Search Tree structure.

"""

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

    def update_height(self):
        """Update the height based on the height of the left and right nodes."""
        node = self
        while node:
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
        """Return next node with larger value"""
        if self.right:
            node = self.right
            while node.left:
                node = node.left
            return node

        node = self
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent

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

    def max_height(self):
        """Return max height from children nodes"""
        if self.left and self.right:
            return max(self.left.height, self.right.height)
        elif self.left:
            return self.left.height
        elif self.right:
            return self.right.height
        else:
            return -1

    def delete_child_or_leaf(self):
        if self.has_child() == None:
            if self.is_right_child():
                self.parent.right = None
                temp = self
                del(self)
                temp.update_height()
                return temp
            if self.is_left_child():
                self.parent.left = None
                temp = self
                del(self)
                temp.update_height()
                return temp

        if self.has_one_child():
            if self == self.parent.left:
                self.parent.left = self.has_child()
                self.has_child().parent = self.parent
                temp = self
                del(self)
                temp.update_height()
                return temp
            if self == self.parent.right:
                self.parent.right = self.has_child()
                self.has_child().parent = self.parent
                temp = self
                del(self)
                temp.update_height()
                return temp

    def __str__(self):
        """Returns the string representation of the node in format: 'key/value'.
           If no value is stored, the representation is just: 'key'."""
        if not self.value:
            return "{0}".format(self.key)
        else:
            return "{0}/{1}".format(self.key, self.value)

    def __repr__(self):
        if not self.value:
            return "Node({0})".format(self.key)
        else:
            return "{0}/{1}".format(self.key, self.value)
