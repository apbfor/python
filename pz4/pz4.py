# -*- coding: utf-8 -*-
"""
В этом модуле реализованы функции,
для выполенения заданий из ПЗ4
"""
import random


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


class Guesser:
    """Play a 'guess a number' game"""

    def __init__(self):
        """Init a random number for guesser"""
        self.rnd = random.randint(0, 100)

    def check(self, guess):
        """Check if guess was right
        Args:
            guess: str from user that guess a number

        Returns:
            0 if correct
            1 if guess > self.rnd
            -1 if guess < self.rnd

        Raises:
            ValueError: if guess cant be converted to int.
        """
        if guess == self.rnd:
            return 0
        if guess > self.rnd:
            return 1
        return -1

    def play(self):
        """Start a guess game"""
        while True:
            answer = input('Угадайте число: ')
            if answer == 'exit':
                break
            if not isinstance(answer, int):
                raise ValueError("Вы ввели не число")
            check = self.check(answer)
            if not check:
                print('\nУспех! Верно угадано число {0}'.format(self.rnd))
                break
            elif check == 1:
                print('Бери ниже')
            elif check == -1:
                print('Бери выше')


def run_guesser():
    """Run guesser"""
    guesser = Guesser()
    guesser.play()


if __name__ == '__main__':
    run_guesser()
