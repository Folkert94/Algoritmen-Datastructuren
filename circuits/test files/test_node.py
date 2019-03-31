from node import Node
from flat import Flat
import numpy as np
import csv

l1 = Flat((7, 7, 1))

gate_1 = l1.is_gate((0, 3, 0), 1)
gate_2 = l1.is_gate((6, 3, 0), 2)

gate_3 = l1.is_gate((3, 3, 0), 3)
gate_4 = l1.is_gate((3, 4, 0), 4)
gate_5 = l1.is_gate((3, 5, 0), 5)

l1.find_route(gate_1, gate_2, '01')
print(l1)
