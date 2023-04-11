#!/usr/bin/python3
""" Square class midel definition """


class Square():
    """ Square class """
    width = 0
    height = 0
    
    def __init__(self, *args, **kwargs):
        """ The start of Square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the Square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of square class """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """printable representations"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ Main function of Square class """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())