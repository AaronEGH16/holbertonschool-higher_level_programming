#!/usr/bin/python3
"""
this module contains a definition of sub class
of list MyList and their methods
"""


class MyList(list):
    """
    defines MyList as a subclass of List,
    thus acquiring its properties

    methods:
    print_sorted(self)
    """

    def print_sorted(self):
        """
        print a sorted list
        """
        print(sorted(self))
