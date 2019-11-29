"""
В этом модуле находится простейший
калькулятор, реализующий сложение,
вычитание, деление и умножение
"""


def calc(var1, var2, operation):
    """
    This is calculator .

    Args:
        var1: First int arg.
        var2: Second int arg.
        operation: *,/,-,+ are available

    Returns:
        int value of calculation

    Raises:
        ValueError: Raises an exception while args
        or operation is not correct.
    """

    operations = {
        '+': int.__add__,
        '*': int.__mul__,
        '-': int.__sub__,
        '/': int.__truediv__
    }

    if not isinstance(var1, int) or not isinstance(var2, int):
        raise ValueError("Введенные числа не являются целыми")

    if operation not in operations:
        raise ValueError("Такой операции не существует")
    return operations[operation](var1, var2)


def main():
    """
    main function for run calc
    """
    try:
        print(calc('g', 12, '+'))
    except ValueError as exc:
        print("Problem with: ", exc.args[0])

    try:
        print(calc(5, 6, 'p'))
    except ValueError as exc:
        print("Problem with: ", exc.args[0])

    try:
        print(calc(5, 6, '*'))
    except ValueError as exc:
        print("Problem with: ", exc.args[0])


if __name__ == '__main__':
    main()
