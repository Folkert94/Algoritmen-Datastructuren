from node import Node
from bst import BST

print(BST([5, 3, 8]))

# h = BST([5, 8, 12, 18, 100, 3, 1, 6])

# test = list(h.breadth_first_traversal())
# s = ""
#
# s += "{0} \n".format(test[0][0])
# del(test[0])
#
# for i in test[:1]:
#     count = 0
#     for j in i:
#         s += "{0} ".format(j)
#         if j != None:
#             count += 1
# s += "\n"
# del(test[:1])
#
# while test != []:
#     prev = count
#     count = 0
#     for i in test[:prev]:
#         for j in i:
#             if j != None:
#                 s += "{0} ".format(j)
#                 count += 1
#             else:
#                 s += "_ "
#     s += "\n"
#     del(test[:prev])
#
# or_list = h.in_order_traversal()
#
# for i in or_list:
#     s += "{0} ".format(i)
# s += "\n"
#
# print(s)
