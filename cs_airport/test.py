from node import Node
from bst import BST
from avl import AVL

h = AVL([21, 17, 11, 15, 6, 5, 8, 1, 9])

n = h.get_root().get_left_child()

print(n)
print("\n")
print(str(h))
