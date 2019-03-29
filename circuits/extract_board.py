"""
Folkert Stijnman
10475206

Program for extracting board, gates and routes, from csv's.
Runs a 100 times sorting the routes to find the best possible configuration

See comments for adjusting to certain boards and netlists
"""

from node import Node
from flat import Flat
import numpy as np
import random
import csv

# change file to board 1 or 2
csv = open('circuit_board_2.csv', "r").read()

run_time = 0
lowest_fail = 1
total_fail = 0
while run_time < 100:
    route_number = 1

    # adjust for 18x13 or 18x17 board
    l1 = Flat((18, 17, 7))
    gates = []

    rows = csv.split("\n")
    i = 0
    for row in rows:
        # board1: 3 - 29 // board2: 3 - 54
        if i > 3 and i < 54:
            columns = row.split(",")
            gates.append(np.array(columns))
        i += 1
    for gate in np.array(gates):
        l1.is_gate((int(gate[1]), int(gate[2]), 0), gate[0])


    routes = []
    j = 0
    for row in rows:
        # board 1 : 1{31 - 62} // 2{64 - 105} // 3{107 - 158}
        # board 2 : 1{56 - 107} // 2{109 - 170} // 3{172 - 243}
        if j > 172 and j < 243:
            columns = row.split(",")
            routes.append(np.array(columns))
        j += 1
    random.shuffle(routes)
    failed_routes = 0
    for route in routes:
        route_num = ''
        if route_number < 10:
            route_num = '0'
        route_num += str(route_number)
        gate1 = l1.find_gate(int(route[0]))
        gate2 = l1.find_gate(int(route[1]))
        if l1.find_route(gate1, gate2, route_num) is None:
            failed_routes += 1
        route_number += 1
    # set divisor to number of routes
    average_fail = failed_routes / 70

    # get best solution possible
    if average_fail < lowest_fail:
        print('better')
        f = open('output.txt','w')
        print(l1, file=f)
        lowest_fail = average_fail
    run_time += 1
