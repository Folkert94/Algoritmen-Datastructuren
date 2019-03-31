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
    # board1 gates: 3 - 29 // board2 gates: 3 - 54
    if i > 3 and i < 29:
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
    if j > 31 and j < 62:
        columns = row.split(",")
        routes.append(np.array(columns))
    j += 1

gate_1 = l1.find_gate(24)
gate_2 = l1.find_gate(5)

l1.find_route(gate_1, gate_2, '01')
print(l1)
