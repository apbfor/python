import unittest
from calc import calc


class TestCalc(unittest.TestCase):
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
        should_ans = [10/20, 1, 2, -10/20]
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


if __name__ == '__main__':
    unittest.main()
