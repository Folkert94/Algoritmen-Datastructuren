from node import Node
from flat import Flat
import numpy as np
import random
import csv

csv = open('circuit_board_1.csv', "r").read()

l1 = Flat((18, 13, 7))
gates = []

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

route_number = 1
failed_routes = 0
length = 0
for route in routes:
    if route_number < 31:
        route_num = ''
        if route_number < 10:
            route_num = '0'
        route_num += str(route_number)
        gate1 = l1.find_gate(int(route[0]))
        gate2 = l1.find_gate(int(route[1]))
        made_route = l1.find_route(gate1, gate2, route_num)
        if made_route is None:
            failed_routes += 1
        else:
            length += len(made_route)
    route_number += 1


print(l1)
print(failed_routes)
print(length)
f = open('output.txt','w')
print(l1, file=f)
