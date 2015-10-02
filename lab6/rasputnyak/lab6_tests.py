import unittest
import lab6
import random

class TestSorting(unittest.TestCase):
    def test_empty(self):
        lst = []
        result = lab6.radix_sort(lst)
        expect = []
        self.assertFalse(not result)
        self.assertEqual(expect, result)

    def test_same(self):
        lst = [3, 67, 41, 3, 3]
        result = lab6.radix_sort(lst)
        expect = [3, 3, 3, 41, 67]
        self.assertEqual(expect, result)

    def test_sorted(self):
        lst = [1, 2, 3, 4, 5]
        result = lab6.radix_sort(lst)
        expect = [1, 2, 3, 4, 5]
        self.assertEqual(expect, result)

    def test_unsorted(self):
        lst = [5, 4, 3, 2, 1]
        result = lab6.radix_sort(lst)
        expect = [1, 2, 3, 4, 5]
        self.assertEqual(expect, result)

    def test_random(self):
        lst = [random.randint(0, 1000) for i in range(6)]
        result = lab6.radix_sort(lst)
        lst.sort()
        self.assertEqual(lst, result)

