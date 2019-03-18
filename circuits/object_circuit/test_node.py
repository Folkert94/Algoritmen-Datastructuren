from node import Node
from layer import Layer
import numpy as np
import csv

l1 = Layer((13, 13))

gate_24 = l1.is_gate((1, 11), 24)
gate_5 = l1.is_gate((3, 2), 5)
print(l1.find_route(gate_24, gate_5))

print(l1)
