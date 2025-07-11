#!/usr/bin/python3
"""This modulss MyList that inherits from the built-in list class.
It includes a method to print the list sorted in ascending order.
"""


class MyList(list):
    """
    MyList inherits from the built-in list class.
    Adds a public instance mst sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints ending sorted order without modifying the original list.
        """
        print(sorted(self))
