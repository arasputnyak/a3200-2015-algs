import unittest
import lab10

class TestTriple(unittest.TestCase):
    def empty_lst(self):
        lst = []
        result = lab10.triple(lst)
        expected = 0
        self.assertEqual(result, expected)

    def no_triple(self):
        lst = [3, 4, 7]
        result = lab10.triple(lst)
        expected = 0
        self.assertEqual(result, expected)

    def trivial_triple(self):
        lst = [3, 4, 5]
        result = lab10.triple(lst)
        expected = 1
        self.assertEqual(result, expected)

    def example_triple(self):
        lst = [23, 247, 19, 96, 264, 265, 132, 181]
        result = lab10.triple(lst)
        expected = 2
        self.assertEqual(result, expected)