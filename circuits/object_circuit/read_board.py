from node import Node
from layer import Layer
import numpy as np
import csv

l1 = Layer((18, 13))
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
    l1.is_gate((int(gate[1]), int(gate[2])), gate[0])

gate1 = l1.find_gate(4)
gate2 = l1.find_gate(24)

l1.find_route(gate1, gate2)

# l1.find_route(gate_24, gate_5)

print(l1)
