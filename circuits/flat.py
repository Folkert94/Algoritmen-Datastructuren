"""
Folkert Stijnman    10475206

Flat class for layers of nodes in given dimensions

"""
import random
import numpy as np
from node import Node

class Flat(object):
    def __init__(self, dimensions):
        """Initializing grid. Usage: Flat((18, 5, 4))"""
        self.origin = None
        self.dimensions = dimensions
        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                for z in range(dimensions[2]):
                    if z == 0:
                        self.insert_ground_floor((x, y, z))
                    else:
                        self.insert_upper_floors((x, y, z))

    def insert_ground_floor(self, coordinates):
        """Insert ground floor"""
        if sum(coordinates) == 0:
            return self.insert_origin()
        if coordinates[0] == 0:
            return self.insert_y_axis(coordinates)
        if coordinates[1] == 0:
            return self.insert_x_axis(coordinates)
        else:
            return self.insert_regular(coordinates)

    def insert_upper_floors(self, coordinates):
        """Insert upper floor"""
        if coordinates[0] + coordinates[1] == 0:
            return self.insert_origin_z(coordinates)
        if coordinates[0] == 0:
            return self.insert_upper_y_axis(coordinates)
        if coordinates[1] == 0:
            return self.insert_upper_x_axis(coordinates)
        else:
            self.insert_upper_regular(coordinates)

    def insert_upper_regular(self, coordinates):
        """Insert regular node in upper floor"""
        node = self.origin
        i = 0
        while node.up != None and i < coordinates[2]:
            node = node.up
            i += 1
        j = 0
        while node.north != None and j < coordinates[1]:
            node = node.north
            j += 1
        k = 0
        while node.east != None and k < coordinates[0]:
            node = node.east
            k += 1
        node.east = Node(coordinates)
        node.east.west = node

        node_south = self.find_node((coordinates[0], coordinates[1] - 1, coordinates[2]))
        node_down = self.find_node((coordinates[0], coordinates[1], coordinates[2] - 1))

        node.east.south = node_south
        node_south.north = node.east

        node.east.down = node_down
        node_down.up = node.east

        return node.east

    def insert_upper_x_axis(self, coordinates):
        """Insert upper x axis"""
        node = self.origin
        i = 0
        while node.up != None and i < coordinates[2]:
            node = node.up
            i += 1
        j = 0
        while node.east != None and j < coordinates[0]:
            node = node.east
            j += 1

        node.east = Node(coordinates)
        node.east.west = node
        node_down = self.find_node((coordinates[0], coordinates[1], coordinates[2] - 1))
        node.east.down = node_down
        node_down.up = node.east
        return node.east

    def insert_upper_y_axis(self, coordinates):
        """Insert upper y axis"""
        node = self.origin
        i = 0
        while node.up != None and i < coordinates[2]:
            node = node.up
            i += 1
        j = 0
        while node.north != None and j < coordinates[1]:
            node = node.north
            j += 1

        node.north = Node(coordinates)
        node.north.south = node
        node_down = self.find_node((coordinates[0], coordinates[1], coordinates[2] - 1))
        node.north.down = node_down
        node_down.up = node.north
        return node.north

    def insert_origin_z(self, coordinates):
        """Insert origin on higher floors"""
        i = 0
        node = self.origin
        while node.up != None and i < coordinates[2]:
            node = node.up
            i += 1
        node.up = Node(coordinates)
        node.up.down = node
        return node.up

    def insert_origin(self):
        """Insert a origin node"""
        self.origin = Node((0,0,0))
        return self.origin

    def insert_y_axis(self, coordinates):
        """Insert a node on the ground floor on y-axis"""
        node = self.origin
        i = 0
        while node.north != None and i < coordinates[1]:
            node = node.north
            i += 1
        node.north = Node((coordinates))
        node.north.south = node
        return node.north

    def insert_x_axis(self, coordinates):
        """Insert a node on the ground floor on x-axis"""
        node = self.origin
        i = 0
        while node.east != None and i < coordinates[0]:
            node = node.east
            i += 1
        node.east = Node((coordinates))
        node.east.west = node
        return node.east

    def insert_regular(self, coordinates):
        """Inserts regular node on ground floor that is not on the x-axis
        or on the y-axis"""
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
        """Returns node given the coordinates"""
        node = self.origin
        if node == None:
            return None
        z = 0
        while node.up and z < coordinates[2]:
            node = node.up
            z += 1
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
        return node

    def is_gate(self, coordinates, gate_num):
        """Sets node to given gate number given coordinates of the node
        and return the node"""
        node = self.find_node(coordinates)
        node.gate = True
        node.gate_num = gate_num
        return node

    def get_origin(self):
        """Returns origin"""
        return self.origin

    def lowest_density(self):
        """Returns the layer index with lowest density"""
        densities = []
        node = self.get_origin()
        while node != None:
            densities.append(self.layer_density(node))
            node = node.up
        y = 1
        index = 0
        for x in densities:
            if x < y:
                x = y
            index += 1
        return index

    def layer_density(self, node):
        """Find the layer density of a layer given a node"""
        start_node = node
        layer_num = node.coordinates[2]
        square_pt = self.dimensions[0] * self.dimensions[1]
        layer_weight = 0
        i = 0
        node = self.origin
        while node.up and i < layer_num:
            node = node.up
            i += 1
        while node:
            temp = node
            while node:
                if node.route != 'No Route':
                    layer_weight += 1
                if node.gate is True:
                    layer_weight += 5
                node = node.east
            node = temp.north
        return layer_weight / square_pt

    def find_route(self, start_node, goal_node, route_num):
        """Finds route between given start and goal node if route becomes too
        long or open and closed list become 0, not route is found."""
        open_list = []
        closed_list = []
        seen = []
        node = start_node

        min_distance = start_node.man_distance(goal_node)
        closed_list.append(node)

        while node != goal_node:
            if len(closed_list) > min_distance + 50:
                return None

            for adj_node in node.find_adjacent(goal_node):

                adj_node.gcost = 1 + 2 * self.layer_density(adj_node)

                adj_node.hcost = adj_node.man_distance(goal_node)
                adj_node.fcost = adj_node.gcost + adj_node.hcost

                # if it can only go back
                if adj_node.find_adjacent(goal_node) == [node]:
                    pass

                # if there is a route or gate skip it
                if str(adj_node.route) != 'No Route' and adj_node.gate == False:
                    pass
                else:
                    open_list.append(adj_node)
            open_list = set(open_list) - set(closed_list) - set(seen)
            open_list = list(open_list)
            if len(open_list) == 0:
                if len(closed_list) == 0:
                    return None
                seen.append(closed_list[-1])
                del closed_list[-1]
                continue

            node = open_list[-1]
            for x in open_list:
                if x.fcost < node.fcost:
                    node = x
                    open_list.remove(x)
            closed_list.append(node)
            open_list = []

        for y in closed_list:
            y.route = route_num

        return closed_list

    def find_route_sub_goal(self, start_node, goal_node, route_num):
        """Finds route between given start and goal node if route becomes too
        long or open and closed list become 0, not route is found."""
        open_list = []
        closed_list = []
        seen = []
        node = start_node

        min_distance = start_node.man_distance(goal_node)
        closed_list.append(node)

        floor = self.lowest_density()
        sub_goal1 = self.find_node((start_node.coordinates[0], start_node.coordinates[1], floor - 1))
        sub_goal2 = self.find_node((goal_node.coordinates[0], goal_node.coordinates[1], floor - 1))

        while node != goal_node:
            if len(closed_list) > min_distance + 50:
                return None
            if sub_goal1 not in closed_list:
                temp_goal = sub_goal1
            if sub_goal1 in closed_list and sub_goal2 not in closed_list:
                temp_goal = sub_goal2
            if sub_goal1 in closed_list and sub_goal2 in closed_list:
                temp_goal = goal_node

            for adj_node in node.find_adjacent(temp_goal):
                adj_node.gcost = 1

                adj_node.hcost = adj_node.man_distance(temp_goal)
                adj_node.fcost = adj_node.gcost + adj_node.hcost

                # if it can only go back
                if adj_node.find_adjacent(temp_goal) == [node]:
                    pass

                # if there is a route or gate skip it
                if str(adj_node.route) != 'No Route' and adj_node.gate == False:
                    pass
                else:
                    open_list.append(adj_node)
            open_list = set(open_list) - set(closed_list) - set(seen)
            open_list = list(open_list)
            if len(open_list) == 0:
                if len(closed_list) == 0:
                    return None
                seen.append(closed_list[-1])
                del closed_list[-1]
                continue

            node = open_list[-1]
            for x in open_list:
                if x.fcost < node.fcost:
                    node = x
                    open_list.remove(x)
            closed_list.append(node)
            open_list = []

        for y in closed_list:
            y.route = route_num

        return closed_list

    def find_rand_sub_goal(self, start_node, goal_node, route_num):
        """Finds route between given start and goal node if route becomes too
        long or open and closed list become 0, no route is found."""
        open_list = []
        closed_list = []
        seen = []
        node = start_node

        min_distance = start_node.man_distance(goal_node)
        closed_list.append(node)

        floor = self.lowest_density()
        sub_goal1 = self.find_node((random.randint(start_node.coordinates[0], self.dimensions[0]-1), random.randint(start_node.coordinates[1], self.dimensions[1]-1), floor - 1))
        sub_goal2 = self.find_node((random.randint(goal_node.coordinates[0], self.dimensions[0]-1), random.randint(goal_node.coordinates[1], self.dimensions[1]-1), floor - 1))

        while node != goal_node:
            if len(closed_list) > min_distance + 50:
                return None
            if sub_goal1 not in closed_list:
                temp_goal = sub_goal1
            if sub_goal1 in closed_list and sub_goal2 not in closed_list:
                temp_goal = sub_goal2
            if sub_goal1 in closed_list and sub_goal2 in closed_list:
                temp_goal = goal_node

            for adj_node in node.find_adjacent(temp_goal):

                adj_node.gcost = 1

                adj_node.hcost = adj_node.man_distance(temp_goal)
                adj_node.fcost = adj_node.gcost + adj_node.hcost

                # if it can only go back
                if adj_node.find_adjacent(temp_goal) == [node]:
                    pass

                # if there is a route or gate skip it
                if str(adj_node.route) != 'No Route' and adj_node.gate == False:
                    pass
                else:
                    open_list.append(adj_node)
            open_list = set(open_list) - set(closed_list) - set(seen)
            open_list = list(open_list)
            if len(open_list) == 0:
                if len(closed_list) == 0:
                    return None
                seen.append(closed_list[-1])
                del closed_list[-1]
                continue

            node = open_list[-1]
            for x in open_list:
                if x.fcost < node.fcost:
                    node = x
                    open_list.remove(x)
            closed_list.append(node)
            open_list = []

        for y in closed_list:
            y.route = route_num

        return closed_list

    def __str__(self):
        grid_string = ""
        node = self.origin
        if node == None:
            return None
        layer = 1
        while node != None:
            grid_string += "### Layer {0} ###\n".format(layer)
            temp_floor = node
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
            grid_string += "\n"
            node = temp_floor.up
            layer += 1
        return grid_string
