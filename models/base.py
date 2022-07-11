#!/usr/bin/python3
"""Modules for class base
It takes a private instance object
"""


class Base:
    """Declaring the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Defining the class constructor
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
