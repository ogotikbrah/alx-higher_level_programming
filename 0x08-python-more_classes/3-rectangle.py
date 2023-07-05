#!/usr/bin/python3
"""DEfine class Rectangle"""

class Rectangle:
    """Class rectangle: it will define the properties:
        Attributes: 
        width: rep width of the rectangle
        height: rep height of the rect:
        """

    def __init__(self, width=0, height=0):
        """Method that will be called everytime when class rectangle is instaciated
         Args:
         width: default value of 0
         height: default value of o
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the getter method for width
        
        return: the obj
        """
        return self.__width

    @width.setter
    def width(self, value):
        """the setter method for width
        args: 
            value(int)
        raise:
            TypeError: if not type(value==0)
            ValueError: value < 0
        """
        if not issubclass(type(value), int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width  = value

