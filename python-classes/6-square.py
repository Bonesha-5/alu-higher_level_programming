#!/usr/bin/python3
"""Defines a Square class with size and position."""


class Square:
    """Square class with size and position attributes, area calculation, and print."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with size and position.

        Args:
            size (int): size of the square (default 0)
            position (tuple): tuple of two positive integers (default (0, 0))

        Raises:
            TypeError: if size or position are invalid.
            ValueError: if size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): new size value

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): tuple of two positive integers

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple)
            len(value) != 2 or

            not isinstance(value[0], int) or

            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0) or:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character # respecting position.

        Prints an empty line if size is 0.
        Position is used for horizontal and vertical offset.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
