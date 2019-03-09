from node import Node
from bst import BST
from avl import AVL

h = AVL([50, 30, 70, 20, 40, 60, 80])
h.delete(20)
h.delete(30)
# h.delete(50)

print(str(h))
