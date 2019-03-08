from node import Node

class BST(object):
    def __init__(self, key_list=[]):
        """Create a new BST, set its attributes, and insert all the keys in
           the key_list into the BST."""
        self.root = None
        for i in range(len(key_list)):
            self.insert(key_list[i])


    def get_root(self):
        """Return the root of the BST."""
        return self.root

    def is_empty(self):
        """Return True if the BST is empty."""
        if self.root == None:
            return True

    def find_max(self):
        """Return the node with the maximum key in the BST."""
        node = self.get_root()
        if node == None:
            return None
        if node.has_child() == None:
            return node
        while node.get_right_child() != None:
            node = node.get_right_child()
        return node


    def find_min(self):
        """Return the node with the minimum key in the BST."""
        node = self.get_root()
        if node == None:
            return None
        if node.has_child() == None:
            return node
        while node.get_left_child() != None:
            node = node.get_left_child()
        return node

    def search(self, key):
        """Return the Node object containing the key if the key exists in
           the BST, else return None."""
        node = self.get_root()
        if node == None:
            return None
        if key == node:
            return node
        while node.has_child() != None:
            if key < node and node.get_left_child() != None:
                node = node.get_left_child()
                continue
            if key > node and node.get_right_child() != None:
                node = node.get_right_child()
                continue
            else:
                break
        if node != None and node.key == key:
            return node
        else:
            return None


    def contains(self, key):
        """ Return True if the key exists in the BST, else return False."""
        if self.search(key) == key:
            return True
        else:
            return False

    def insert(self, key, value=None):
        """Create a new node for this key and value, and insert it into the BST.

           Return the new inserted node, or None if the key and value could not
           be inserted."""
        if self.contains(key):
            return None
        if self.root:
            return self._insert(self.root, Node(key, value))
        else:
            self.root = Node(key, value)
            self.root.height = 0
            return self.root

    def _insert(self, node, new_node):
        """Recursive function for insert"""
        if new_node < node.key:
            if node.get_left_child():
                return self._insert(node.left, new_node)
            else:
                node.left = new_node
                new_node.parent = node
                new_node.update_height()
                return new_node
        else:
            if node.get_right_child():
                return self._insert(node.right, new_node)
            else:
                node.right = new_node
                new_node.parent = node
                new_node.update_height()
                return new_node

    def delete(self, key):
        """Remove the Node object containing the key if the key exists in
           the BST and return the removed node, else return None.

           The returned node is the actual Node object that got removed
           from the BST, and so might be successor of the removed key."""
        node = self.search(key)
        if node.has_child() == None:
            if node.is_right_child():
                node.parent.right = None
                temp = node
                del(node)
                return temp
            if node.is_left_child():
                node.parent.left = None
                temp = node
                del(node)
                return temp


    def in_order_traversal(self):
        """Return a list of the Nodes in the tree in sorted order."""
        array = []
        node = self.find_min()
        array.append(node)
        while node.next() != None:
            node = node.next()
            array.append(node)
        return(array)

    def breadth_first_traversal(self, height=1):
        """Return a list of lists, where each inner lists contains the elements
           of one layer in the tree. Layers are filled in breadth-first-order,
           and contain contain all elements linked in the BST, including the
           None elements.
           >> BST([5, 8]).breadth_first_traversal()
           [[Node(5)], [None, Node(8)], [None, None]]"""

        root = self.root
        mem = []
        witte_lijst = [[root]]
        mem.append(root)
        while mem:
            temp = []
            current = mem.pop(0)
            if current.left:
                mem.append(current.left)
                temp.append(current.get_left_child())
            if current.left == None:
                temp.append(None)
            if current.right:
                mem.append(current.right)
                temp.append(current.get_right_child())
            if current.right == None:
                temp.append(None)
            witte_lijst.append(temp)
        return witte_lijst

    def __str__(self):
        """Return a string containing the elements of the tree in breadth-first
           order, with each on a new line, and None elements as `_`, and
           finally a single line containing all the nodes in sorted order.
           >> print(BST([5, 8, 3]))
           5
           3 8
           _ _ _ _
           3 5 8
           """
        test = list(self.breadth_first_traversal())
        s = ""

        s += "{0} \n".format(test[0][0])
        del(test[0])

        for i in test[:1]:
            count = 0
            for j in i:
                if j != None:
                    s += "{0} ".format(j)
                    count += 1
                else:
                    s += "_ "
        s += "\n"
        del(test[:1])

        while test != []:
            prev = count
            count = 0
            for i in test[:prev]:
                for j in i:
                    if j != None:
                        s += "{0} ".format(j)
                        count += 1
                    else:
                        s += "_ "
            s += "\n"
            del(test[:prev])

        or_list = self.in_order_traversal()

        for i in or_list:
            s += "{0} ".format(i)

        return s
