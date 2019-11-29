# -*- coding: utf-8 -*-
"""
Модуль с тестами для ПЗ4
"""
import unittest
from unittest.mock import patch
from pz4 import calc
from pz4 import Guesser


class TestCalc(unittest.TestCase):
    """
    Тесты для калькулятора
    """
    def test_calc_add(self):
        a = [10, 20, 40, -10]
        b = 20
        should_ans = [30, 40, 60, 10]
        for i in range(len(a)):
            res = calc(a[i], b, '+')
            self.assertEqual(res, should_ans[i])

    def test_calc_multiply(self):
        a = [10, 20, 40, -10]
        b = 20
        should_ans = [200, 400, 800, -200]
        for i in range(len(a)):
            res = calc(a[i], b, '*')
            self.assertEqual(res, should_ans[i])

    def test_calc_div(self):
        a = [10, 20, 40, -10]
        b = 20
        should_ans = [0.5, 1, 2, -0.5]
        for i in range(len(a)):
            res = calc(a[i], b, '/')
            self.assertEqual(res, should_ans[i])

    def test_calc_sub(self):
        a = [10, 20, 40, -10]
        b = 20
        should_ans = [-10, 0, 20, -30]
        for i in range(len(a)):
            res = calc(a[i], b, '-')
            self.assertEqual(res, should_ans[i])

    def test_calc_not_integer(self):
        a = 'a'
        b = 10
        op = '+'
        with self.assertRaises(ValueError):
            res = calc(a, b, op)

    def test_calc_invalid_operation(self):
        a = 5
        b = 15
        op = 's'
        with self.assertRaises(ValueError):
            res = calc(a, b, op)


class TestGuesser(unittest.TestCase):
    """Класс, содержащий тесты для угадайки"""
    def test_check(self):
        """Основной тест"""
        rnd = 15
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = 15
        should_ans = 0
        self.assertEqual(guesser.check(guess), should_ans)

    def test_map(self):
        """Те же тесты, но в словарике"""
        rnd = [5, 10, 15, 30, 45, 60, 100]
        guess = [5, 10, 15, 30, 45, 60, 100]
        should_ans = 0
        for ind, item in enumerate(rnd):
            with patch('random.randint', return_value=item):
                guesser = Guesser()
            self.assertEqual(guesser.check(guess[ind]), should_ans)

    def test_return(self):
        rnd = 50
        with patch('random.randint', return_value=rnd):
            guesser = Guesser()
        guess = 30
        should_ans = -1
        self.assertEqual(guesser.check(guess), should_ans)
        guess = 60
        should_ans = 1
        self.assertEqual(guesser.check(guess), should_ans)

    def test_play(self):
        """change user input"""
        with patch('random.randint', return_value=15):
            with patch('builtins.input', return_value=15):
                guess = Guesser()
                self.assertEqual(guess.play(), None)

    def test_play_error(self):
        """check error"""
        with patch('builtins.input', return_value='abcdefg'):
            with self.assertRaises(ValueError):
                guess = Guesser()
                guess.play()


if __name__ == '__main__':
    unittest.main()
