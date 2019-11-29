"""Модуль с Mock тестами для угадайки"""
import unittest
from unittest.mock import patch
from guesser import Guesser


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
