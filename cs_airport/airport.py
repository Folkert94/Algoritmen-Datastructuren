"""
Folkert Stijnman

10475206

Datastructuren & Algoritmen

Airport implementation using BST and Airport.

"""

import argparse

from bst import BST
class Airport(BST):
    def __init__(self, wait_time=300000, simple=False):
        BST.__init__(self)
        self.wait_time = wait_time
        self.simple = simple

    def find_conflict(self, time):
        """Return the first node in the tree that conflicts with the specified
           time and wait_time attribute set for the Airport.

           Returns None if no such conflict is found."""
        node = self.get_root()

        if node is None:
            return None

        while node != None:
            if abs(node.key - time) < self.wait_time:
                return node
            elif time < node.key:
                node = node.left
            elif time > node.key:
                node = node.right
        return None

    def bounded_insert(self, time, tailnumber):
        """Inserts a airplane with a time and tailnumber into the schedule.
           If the difference between the proposed time and an existing node
           in schedule is less then the wait_time, the airplane cannot be
           scheduled at that time.

           If the simple flag is set to True, conflict are not inserted
           and otherwise the program will try to insert in the next
           possible timeslot.

           Returns the node if successfully inserted and None otherwise."""
        if self.simple is True:
           if self.find_conflict(time) is not None:
               return None

        while self.find_conflict(time) != None:
            node = self.find_conflict(time)
            time = node.key + self.wait_time

        node = BST.insert(self, time, tailnumber)
        return node

    def __str__(self):
        """Return the airplanes in the schedule in sorted order."""
        s = ""
        for i in self.in_order_traversal():
            s += "{0}/{1} ".format(i.key, i.value)
        return s.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort a list of elements.')
    parser.add_argument('elements', nargs='+',
                    help='The elements of a list')
    parser.add_argument("-t", "--timestep", type=int,
                    help="set the minimum timestep (default=300000)", default=300000)
    parser.add_argument("-s", "--simple", action="store_true",
                    help="either become simple or not")
    args = parser.parse_args()

    cs_airport = Airport(args.timestep, args.simple)
    for elem in args.elements:
        try:
            s = elem.split('/')
            time, tail = int(s[0]), s[1]
            cs_airport.bounded_insert(time, tail)
        except (ValueError, IndexError):
            print("Invalid airplane format: "+elem)

    print(cs_airport)
