from math import pi


class Figure:
    def draw(self):
        pass

    def __init__(self, size):
        self.size = size


class Circle(Figure):
    def __init__(self, size):
        Figure.__init__(self, size)

    def __str__(self):
        return "Circle"

    def __repr__(self):
        return "This is Circle"

    def draw(self):
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
    def __init__(self, size):
        Figure.__init__(self, size)

    def __str__(self):
        return "Ellipse"

    def __repr__(self):
        return "This is Ellipse"

    def draw(self):
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
        for i in range(int(self.size)*2):
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
    """Minimum size = 6"""
    def __init__(self, size):
        Figure.__init__(self, size)

    def __str__(self):
        return "Square"

    def __repr__(self):
        return "This is square"

    def draw(self):
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
