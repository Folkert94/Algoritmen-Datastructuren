from node import Node
from flat import Flat
import numpy as np
import random
import csv



csv = open('circuit_board_1.csv', "r").read()

run_time = 0
total_fail = 0
while run_time < 1000:
    route_number = 1
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
    random.shuffle(routes)
    failed_routes = 0
    for route in routes:
        if route_number < 31:
            route_num = ''
            if route_number < 10:
                route_num = '0'
            route_num += str(route_number)
            gate1 = l1.find_gate(int(route[0]))
            gate2 = l1.find_gate(int(route[1]))
            if l1.find_route(gate1, gate2, route_num) is None:
                failed_routes += 1
        route_number += 1
    average_fail = failed_routes / 30
    print(average_fail)
    if average_fail < 0.1:
        break
    total_fail += average_fail
    run_time += 1

print(total_fail / 100)

f = open('output.txt','w')
print(l1, file=f)
