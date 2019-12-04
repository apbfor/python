"""
Module for PZ5
Inside: Drawing figures
"""


class Figure:
    """Superclass for all figures"""
    def draw(self):
        """drawing funcion"""

    def __init__(self, size):
        self.size = size

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Circle(Figure):
    """Class for circles"""
    def __init__(self, size):
        Figure.__init__(self, size)

    def __str__(self):
        return "Circle"

    def __repr__(self):
        return "This is Circle"

    def draw(self):
        """Draws one circle any size"""
        print('  ', end='')  # magic value
        for i in range(self.size+1):
            print('*', end='  ')
        print()
        print(' ', end='')
        print('*', end='')
        for i in range(int(self.size)*3+1):
            print(' ', end='')
        print('*', end='')
        print()
        for i in range(self.size):
            print('*', end='')
            for j in range(int(self.size)*3+3):
                print(' ', end='')
            print('*')
        print(' ', end='')
        print('*', end='')
        for i in range(int(self.size)*3 + 1):
            print(' ', end='')
        print('*', end='')
        print()
        print('  ', end='')  # magic value
        for i in range(self.size + 1):
            print('*', end='  ')
        print()


class Ellipse(Figure):
    """class for ellipses"""
    def __init__(self, size):
        Figure.__init__(self, size)

    def __str__(self):
        return "Ellipse"

    def __repr__(self):
        return "This is Ellipse"

    def draw(self):
        """draw one ellipse current size"""
        print('  ', end='')  # magic value
        for i in range(self.size + 1):
            print('*', end='  ')
        print()
        print(' ', end='')
        print('*', end='')
        for i in range(int(self.size) * 3 + 1):
            print(' ', end='')
        print('*', end='')
        print()
        for i in range(int(self.size)*3):
            print('*', end='')
            for j in range(int(self.size) * 3 + 3):
                print(' ', end='')
            print('*')
        print(' ', end='')
        print('*', end='')
        for i in range(int(self.size) * 3 + 1):
            print(' ', end='')
        print('*', end='')
        print()
        print('  ', end='')  # magic value
        for i in range(self.size + 1):
            print('*', end='  ')
        print()


class Square(Figure):
    """
    class for square
    Minimum size = 6
    """
    def __init__(self, size):
        Figure.__init__(self, size)

    def __str__(self):
        return "Square"

    def __repr__(self):
        return "This is square"

    def draw(self):
        """draw one square current size"""
        for i in range(self.size+1):
            print('*', end='')
        print()
        for i in range(int(self.size/2) - 2):
            print('*', end='')
            for j in range(self.size-1):
                print(' ', end='')
            print('*')
        for i in range(self.size+1):
            print('*', end='')
        print()


def main():
    """main func for run all this code"""
    square = Square(12)
    square.draw()
    circle = Circle(3)
    circle.draw()
    print()
    ellipse = Ellipse(4)
    ellipse.draw()
    col = [square, circle, ellipse]
    for i in col:
        print(i)
    print(col)


if __name__ == '__main__':
    main()
