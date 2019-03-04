class Node(object):
    def __init__(self, key, value=None):
        """Store the key and value in the node and set the other attributes."""
        pass
    
    def get_key(self):
        """Return the key of this node."""
        pass
    
    def get_value(self):
        """Return the value of this node."""
        pass
    
    def get_parent(self):
        """Return the parent node of this node."""
        pass
    
    def get_left_child(self):
        """Return the left child node of this node."""
        pass
    
    def get_right_child(self):
        """Return the right child node of this node."""
        pass
    
    def get_height(self):
        """Return the height of this node."""
        pass
    
    def update_height(self):
        """Update the height based on the height of the left and right nodes."""
        pass
    
    #
    # You can add any additional node functions you might need here
    #
    
    def __eq__(self, other):
        """Returns True if the node is equal the other node or value."""
        pass
    
    def __neq__(self, other):
        """Returns True if the node is not equal the other node or value."""
        pass
    
    def __lt__(self, other):
        """Returns True if the node is less than the other node or value."""
        pass
    
    def __le__(self, other):
        """Returns True if the node is less or equal to the other node or value."""
        pass
    
    def __gt__(self, other):
        """Returns True if the node is greater than the other node or value."""
        pass
    
    def __ge__(self, other):
        """Returns True if the node is greater or equal to the other node or value."""
        pass
    
    def __str__(self):
        """Returns the string representation of the node in format: 'key/value'.
           If no value is stored, the representation is just: 'key'."""
        pass

