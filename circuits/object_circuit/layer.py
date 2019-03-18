"""
Folkert Stijnman    10475206

Layer class for layer of nodes in given dimensions

"""
import numpy as np
from node import Node

class Layer(object):
    def __init__(self, dimensions):
        """Initializing grid. Usage Layer((18, 13))"""
        self.origin = None
        self.dimensions = dimensions
        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                self.insert((x, y))

    def insert(self, coordinates):
        if sum(coordinates) == 0:
            return self.insert_origin()
        if coordinates[0] == 0:
            return self.insert_y_axis(coordinates)
        if coordinates[1] == 0:
            return self.insert_x_axis(coordinates)
        else:
            return self.insert_regular(coordinates)

    def insert_origin(self):
        self.origin = Node((0,0))
        return self.origin

    def insert_y_axis(self, coordinates):
        node = self.origin
        while node.north != None:
            node = node.north
        node.north = Node((coordinates))
        node.north.south = node
        return node.north

    def insert_x_axis(self, coordinates):
        node = self.origin
        while node.east != None:
            node = node.east
        node.east = Node((coordinates))
        node.east.west = node
        return node.east

    def insert_regular(self, coordinates):
        node = self.find_node((coordinates[0] - 1, coordinates[1]))
        if node == None:
            return None
        node.east = Node((coordinates))
        node.east.west = node
        node_south = self.find_node((coordinates[0], coordinates[1] - 1))
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
        node = self.origin
        while node:
            temp = node
            while node:
                if int(node.gate_num) == gate_num:
                    return node
                node = node.east
            node = temp.north


    def find_route(self, start_node, goal_node):
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
            y.route = '01'

        return closed_list, open_list

    def is_gate(self, coordinates, gate_num):
        node = self.find_node(coordinates)
        node.gate = True
        node.gate_num = gate_num
        return node

    def get_origin(self):
        return self.origin

    def __str__(self):
        grid_string = ""
        node = self.origin
        if node == None:
            return None
        while node.north:
            node = node.north
        while node:
            temp = node
            while node:
                if node.gate is False:
                    if node.route is not '':
                        grid_string += "{0} ".format(node.route)
                    else:
                        grid_string += "__ "
                if node.gate is True:
                    grid_string += "GA "
                node = node.east
            grid_string += "\n"
            node = temp.south
        return grid_string
