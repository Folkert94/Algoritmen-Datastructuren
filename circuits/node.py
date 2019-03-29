"""
Folkert Stijnman    10475206

Node class for nodes in layer

"""

class Node(object):
    def __init__(self, coordinates, gate=False):
        """Initializing node. Usage Node((4, 2, 1), True)"""
        self.coordinates = coordinates
        self.route = 'No Route'
        self.gate = gate
        self.gate_num = 0
        self.gcost = 0
        self.hcost = None
        self.fcost = None

        self.west = None
        self.east = None
        self.north = None
        self.south = None
        self.up = None
        self.down = None

    def man_distance(self, other):
        """Input two nodes and calculate the Manhattan distance"""
        c_1 = self.coordinates
        c_2 = other.coordinates
        man_dist = abs(c_1[0] - c_2[0]) + abs(c_1[1] - c_2[1]) + abs(c_1[2] - c_2[2])
        return man_dist

    def find_adjacent(self, goal_node):
        """Find adjacent nodes for pathfinding"""
        adj_list = []
        if self.north and self.north.gate == False or self.north is goal_node:
            adj_list.append(self.north)
        if self.south and self.south.gate == False or self.south is goal_node:
            adj_list.append(self.south)
        if self.west and self.west.gate == False or self.west is goal_node:
            adj_list.append(self.west)
        if self.east and self.east.gate == False or self.east is goal_node:
            adj_list.append(self.east)
        if self.up and self.up.gate == False or self.up is goal_node:
            adj_list.append(self.up)
        if self.down and self.down.gate == False or self.down is goal_node:
            adj_list.append(self.down)
        return adj_list

    def __str__(self):
        if self.gate is False:
            return "{0}".format(self.coordinates)
        if self.gate is True:
            return "{0}, Gate".format(self.coordinates)

    def __repr__(self):
        return "Node({0})".format(self.coordinates)
