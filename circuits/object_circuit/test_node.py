from node import Node
from flat import Flat
import numpy as np
import csv

l1 = Flat((18, 13, 1))

n1 = l1.insert_origin_z((0, 0, 1))
n2 = l1.insert_origin_z((0, 0, 2))

print(n2)

print(l1.get_origin().up.up.down)
