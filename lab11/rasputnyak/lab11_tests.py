import unittest
import lab11

class TestArea(unittest.TestCase):
    def test_empty_lst(self):
        lst = []
        result = lab11.area(lst)
        expected = 0
        self.assertEqual(expected, result)

    def test_one_elem_lst(self):
        lst = []
        lst.append(6)
        result = lab11.area(lst)
        expected = 0
        self.assertEqual(expected, result)

    def test_example_area(self):
        lst = [2,5,1,2,3,4,7,7,6]
        result = lab11.area(lst)
        expected = 10
        self.assertEqual(expected, result)
