import unittest
import lab11

class TestArea(unittest.TestCase):
    def empty_lst(self):
        lst = []
        result = lab11.area(lst)
        expected = 0
        self.assertEqual(expected, result)

    def one_elem_lst(self):
        lst = []
        lst.append(6)
        result = lab11.area(lst)
        expected = 0
        self.assertEqual(expected, result)

    def example_area(self):
        lst = [2,5,1,2,3,4,7,7,6]
        result = lab11.area(lst)
        expected = 10
        self.assertEqual(expected, result)