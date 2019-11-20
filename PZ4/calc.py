"""В этом модуле находится простейший
калькулятор, реализующий сложение,
вычитание, деление и умножение"""


def calc(a, b, op):
    """Функция реализует калькулятор
    используя магические методы класса int"""
    operations = {
        '+': int.__add__,
        '*': int.__mul__,
        '-': int.__sub__,
        '/': int.__truediv__
    }
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Введенный(ые) символ(ы) не являются числами")
        return

    if op in operations:
        return operations[op](a, b)
    else:
        print("Ввели несуществующую операцию")


if __name__ == '__main__':
    print(calc(60, 12, '+'))
