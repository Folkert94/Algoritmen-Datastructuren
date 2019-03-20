"""
Folkert Stijnman    10475206

Layer class for layer of nodes in given dimensions

"""
import numpy as np
from node import Node

class Flat(object):
    def __init__(self, dimensions):
        """Initializing grid. Usage Layer((18, 13))"""
        self.origin = None
        self.dimensions = dimensions
        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                for z in range(dimensions[2]):
                    if z == 0:
                        self.insert_ground_floor((x, y, z))
                    else:
                        self.insert_upper_floors((x, y, z))

    def insert_upper_floors(self, coordinates):
        if sum(coordinates[0] + coordinates[1]) == 0:
            return self.insert_origin_z(coordinates)
        if coordinates[0] == 0:
            return self.insert_upper_y_axis(coordinates)

    # def insert_upper_y_axis(self, coordinates):
    #     node = self.origin()
    #     i = 0
    #     while node.up != None and i < coordinates[2]:
    #         node = node.up
    #     j = 0
    #     while node.north != None and i < coordinates[1]:
    #     pass
    def insert_origin_z(self, coordinates):
        i = 0
        node = self.origin
        while node.up != None and i < coordinates[2]:
            node = node.up
            i += 1
        node.up = Node((coordinates))
        node.up.down = node
        return node.up

    def insert_ground_floor(self, coordinates):
        if sum(coordinates) == 0:
            return self.insert_origin()
        if coordinates[0] == 0:
            return self.insert_y_axis(coordinates)
        if coordinates[1] == 0:
            return self.insert_x_axis(coordinates)
        else:
            return self.insert_regular(coordinates)

    def insert_origin(self):
        self.origin = Node((0,0,0))
        return self.origin

    def insert_y_axis(self, coordinates):
        node = self.origin
        i = 0
        while node.north != None and i < coordinates[1]:
            node = node.north
            i += 1
        node.north = Node((coordinates))
        node.north.south = node
        return node.north

    def insert_x_axis(self, coordinates):
        node = self.origin
        i = 0
        while node.east != None and i < coordinates[0]:
            node = node.east
            i += 1
        node.east = Node((coordinates))
        node.east.west = node
        return node.east

    def insert_regular(self, coordinates):
        node = self.find_node((coordinates[0] - 1, coordinates[1], 0))
        if node == None:
            return None
        node.east = Node((coordinates))
        node.east.west = node
        node_south = self.find_node((coordinates[0], coordinates[1] - 1, 0))
        node.east.south = node_south
        node_south.north = node.east
        return node.east

    def find_node(self, coordinates):
        node = self.origin
        if node == None:
            return None
        y = 0
        while node.north and y < coordinates[1]:
            node = node.north
            y += 1

        x = 0
        while node.east and x < coordinates[0]:
            node = node.east
            x += 1

        if node.coordinates != coordinates:
            return None
        else:
            return node

    def find_gate(self, gate_num):
        """Find the node according to given gate number"""
        node = self.origin
        while node:
            temp = node
            while node:
                if int(node.gate_num) == gate_num:
                    return node
                node = node.east
            node = temp.north

    def is_gate(self, coordinates, gate_num):
        """Sets node to given gate number given coordinates of the node
        and return the node"""
        node = self.find_node(coordinates)
        node.gate = True
        node.gate_num = gate_num
        return node

    def get_origin(self):
        return self.origin


    def find_route(self, start_node, goal_node, route_num):
        """Finds route and returns route in list using A*"""
        open_list = []
        closed_list = []
        node = start_node
        closed_list.append(node)

        while node != goal_node:
            for adj_node in node.find_adjacent(goal_node):
                adj_node.gcost = adj_node.man_distance(node)
                adj_node.hcost = adj_node.man_distance(goal_node)
                adj_node.fcost = adj_node.gcost + adj_node.hcost
                if adj_node.find_adjacent(goal_node) == [node]:
                    pass
                if str(adj_node.route) != 'No Route':
                    pass
                else:
                    open_list.append(adj_node)

            open_list = set(open_list) - set(closed_list)
            open_list = list(open_list)

            node = open_list[0]
            for x in open_list:
                if x.fcost < node.fcost:
                    node = x
                    open_list.remove(x)

            closed_list.append(node)
            open_list = []


        for y in closed_list:
            y.route = route_num

        return closed_list, open_list

    def __str__(self):
        grid_string = ""
        node = self.origin
        if node == None:
            return None

        # start from the top
        while node.north:
            node = node.north
        # every row
        while node:
            temp = node
            # every node in row
            while node:
                if node.gate is False:
                    if str(node.route) != 'No Route':
                        grid_string += "{0} ".format(node.route)
                    else:
                        grid_string += "__ "
                if node.gate is True:
                    grid_string += "GA "
                node = node.east
            grid_string += "\n"
            node = temp.south
        return grid_string
