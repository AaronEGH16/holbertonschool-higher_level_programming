#!/usr/bin/python3
"""

"""


class MyList(list):
    """
    defines MyList as a subclass of List,
    thus acquiring its properties
    """

    def print_sorted(self):
        """
        print a sorted list
        """
        print(sorted(self))
