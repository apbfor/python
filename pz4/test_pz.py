# -*- coding: utf-8 -*-
"""
Модуль с тестами для ПЗ4
"""
import io
import sys
import unittest
from unittest.mock import patch
from pz4.pz4 import calc
from pz4.pz4 import Guesser

class TestCalc(unittest.TestCase):
    """
    Тесты для калькулятора
    """
    def test_calc_add(self):
        """

        :return:
        """
        var1 = [10, 20, 40, -10]
        var2 = 20
        should_ans = [30, 40, 60, 10]
        for i in range(len(var1)):
            res = calc(var1[i], var2, '+')
            self.assertEqual(res, should_ans[i])

    def test_calc_multiply(self):
        """

        :return:
        """
        var1 = [10, 20, 40, -10]
        var2 = 20
        should_ans = [200, 400, 800, -200]
        for i in range(len(var1)):
            res = calc(var1[i], var2, '*')
            self.assertEqual(res, should_ans[i])

    def test_calc_div(self):
        """

        :return:
        """
        var1 = [10, 20, 40, -10]
        var2 = 20
        should_ans = [0.5, 1, 2, -0.5]
        for i in range(len(var1)):
            res = calc(var1[i], var2, '/')
            self.assertEqual(res, should_ans[i])

    def test_calc_sub(self):
        """

        :return:
        """
        var1 = [10, 20, 40, -10]
        var2 = 20
        should_ans = [-10, 0, 20, -30]
        for i in range(len(var1)):
            res = calc(var1[i], var2, '-')
            self.assertEqual(res, should_ans[i])

    def test_calc_not_integer(self):
        """

        :return:
        """
        var1 = 'var1'
        var2 = 'var2'
        op = '+'
        with self.assertRaises(ValueError):
            res = calc(var1, var2, op)

    def test_calc_invalid_operation(self):
        """

        :return:
        """
        var1 = 5
        var2 = 15
        op = 'var1'
        with self.assertRaises(ValueError):
            res = calc(var1, var2, op)


class TestGuesser(unittest.TestCase):
    """Класс, содержащий тесты для угадайки"""
    def test_check(self):
        """Основной тест"""
        rnd = 50
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = [50, 30, 60]
        should_ans = [0, -1, 1]
        for i in range(len(guess)):
            self.assertEqual(guesser.check(guess[i]), should_ans[i])

    def test_map(self):
        """Те же тесты, но в словарике"""
        rnd = [5, 10, 15, 30, 45, 60, 100]
        guess = [5, 10, 15, 30, 45, 60, 100]
        should_ans = 0
        for ind, item in enumerate(rnd):
            with patch('random.randint', return_value=item):
                guesser = Guesser()
            self.assertEqual(guesser.check(guess[ind]), should_ans)

    def test_play(self):
        """change user input"""
        with patch('random.randint', return_value=15):
            with patch('builtins.input', return_value=15):
                guess = Guesser()
                self.assertEqual(guess.play(), None)
                print("work")

    def test_less_greater(self):
        """

        :return:
        """
        answers = [20, 60, 50]
        rnd = 50
        should_ans = ['Бери выше\n', 'Бери ниже\n', '\nУспех! Верно угадано число {0}'.format(rnd)]
        with patch('random.randint', return_value=rnd):
            guess = Guesser()
        with patch('builtins.input', side_effect=answers):
            capt_output = io.StringIO()
            sys.stdout = capt_output
            guess.play()
            sys.stdout = sys.__stdout__
            self.assertEqual(''.join(should_ans), capt_output.getvalue().strip())

    def test_play_error(self):
        """check error"""
        with patch('builtins.input', return_value='abcdefg'):
            with self.assertRaises(ValueError):
                guess = Guesser()
                guess.play()

    def test_play_exit(self):
        """exit"""
        with patch('builtins.input', return_value='exit'):
            guess = Guesser()
            self.assertEqual(guess.play(), None)


if __name__ == '__main__':
    unittest.main()
