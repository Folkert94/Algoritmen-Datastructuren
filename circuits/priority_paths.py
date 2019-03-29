from node import Node
from flat import Flat
import numpy as np
import random
from collections import Counter
import csv

csv = open('circuit_board_1.csv', "r").read()



# print(routes)


run_time = 0
while run_time < 1000:
    l1 = Flat((18, 13, 7))
    gates = []

    rows = csv.split("\n")
    i = 0
    for row in rows:
        if i > 3 and i < 29:
            columns = row.split(",")
            gates.append(columns)
        i += 1
    for gate in np.array(gates):
        l1.is_gate((int(gate[1]), int(gate[2]), 0), gate[0])
    routes = []
    j = 0
    for row in rows:
        if j > 31 and j < 62:
            columns = row.split(",")
            temp = []
            for el in columns:
                if el != '':
                    temp.append(int(el))
            routes.append(temp)
        j += 1
    flat_list = [item for sublist in routes for item in sublist]
    count_list = Counter(flat_list)
    occurences = []
    for x in count_list:
        key = x
        value = count_list[key]
        occurences.append([key, value])
    occurences.sort(key=lambda x: x[1], reverse=True)

    sorted_occurences = []
    for gate_it in occurences:
        for route in routes:
            if gate_it[0] in route:
                if route not in sorted_occurences:
                    sorted_occurences.append(route)
    bad = 0
    route_number = 1
    for route in sorted_occurences:
        if route_number < 31:
            route_num = ''
            if route_number < 10:
                route_num = '0'
            route_num += str(route_number)
            gate1 = l1.find_gate(int(route[0]))
            gate2 = l1.find_gate(int(route[1]))
            made_route = l1.find_route(gate1, gate2, route_num)
            if made_route == None:
                bad += 1
        route_number += 1
    print(bad / 30)
    run_time += 1
    if bad < 0.1:
        f = open('output.txt','w')
        print(l1, file=f)
        exit(1)
