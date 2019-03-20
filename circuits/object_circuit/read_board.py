from node import Node
from flat import Flat
import numpy as np
import csv

l1 = Flat((18, 13, 1))
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

gate_24 = l1.find_gate(24)
gate_5 = l1.find_gate(5)
gate_6 = l1.find_gate(6)
gate_8 = l1.find_gate(8)
gate_2 = l1.find_gate(2)
gate_1 = l1.find_gate(1)
gate_16 = l1.find_gate(16)
gate_22 = l1.find_gate(22)

l1.find_route(gate_24, gate_5, '01')
l1.find_route(gate_6, gate_8, '02')
l1.find_route(gate_2, gate_1, '03')
l1.find_route(gate_16, gate_22, '04')

# l1.find_route(gate_24, gate_5)

print(l1)
