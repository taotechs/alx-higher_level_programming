#!/usr/bin/python3
"""Square module

Contains the definition of a square class.

"""


class Square:
    """Definition of a square object.

    Defines a square object that abstacts a real
    world square

    """
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter and setter for the size attribute. """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square. """
        return self.__size ** 2

    def __eq__(self, other):
        """ defines equal to comparison with other squares """
        return self.area() == other.area()

    def __ne__(self, other):
        """ defines not equal to comparison with other squares """
        return self.area() != other.area()

    def __gt__(self, other):
        """ defines greater than comparison with other squares """
        return self.area() > other.area()

    def __lt__(self, other):
        """ defines less than comparison with other squares """
        return self.area() < other.area()

    def __ge__(self, other):
        """ defines greater than or equal to comparison with other squares """
        return self.area() >= other.area()

    def __le__(self, other):
        """ defines less than or equal to comparison with other squares """
        return self.area() <= other.area()
