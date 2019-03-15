"""

Folkert Stijnman    10475206

Node class for nodes in grid


"""

class Node(object):
    def __init___(self, coordinates, gate=False):
        """Initializing node. Usage Node((4, 2, 1), True)"""
        coordinates = set(self.coordinates)
        gate = self.gate

    def __str__(self):
        if self.gate = False:
            return "{0}, Gate: No".format(self.coordinates)
        if self.gate = True:
            return "{0}, Gate: Yes".format(self.coordinates)
