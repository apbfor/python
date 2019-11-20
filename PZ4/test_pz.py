import unittest
from calc import calc


class TestCalc(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(res, should_ans)


if __name__ == '__main__':
    unittest.main()
