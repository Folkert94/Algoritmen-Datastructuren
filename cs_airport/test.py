from node import Node
from bst import BST

n_1 = Node(7)
n_2 = Node(5)
n_3 = Node(3)
n_4 = Node(8)

h = BST([5, 3, 9, 6, 8])

print(h.get_root().get_right_child().height)
