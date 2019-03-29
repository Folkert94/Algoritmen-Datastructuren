from node import Node
from flat import Flat
import numpy as np
import random
import csv

l1 = Flat((18, 13, 7))
gates = []

csv = open('circuit_board_1.csv', "r").read()
rows = csv.split("\n")
i = 0
for row in rows:
    if i > 3 and i < 29:
        columns = row.split(",")
        gates.append(np.array(columns))
    i += 1
for gate in np.array(gates):
    l1.is_gate((int(gate[1]), int(gate[2]), 0), gate[0])

routes = []
j = 0
for row in rows:
    if j > 31 and j < 62:
        columns = row.split(",")
        routes.append(np.array(columns))
    j += 1

lengths = []
sorted_routes = []
for route in routes:
    gate1 = l1.find_gate(int(route[0]))
    gate2 = l1.find_gate(int(route[1]))
    lengths.append([gate1, gate2, gate1.man_distance(gate2)])
    # i = 0
    # while (i < len(sorted_routes)):
length = 0
# lengths.sort(key=lambda x: x[2])
failed_routes = 0
route_num = 1
for route in lengths:
    if route_num < 31:
        made_route = l1.find_route(route[0], route[1], route_num)
        if made_route is None:
            failed_routes += 1
        else:
            length += len(made_route)
    route_num += 1

print(l1)
print(failed_routes)
print(length)
