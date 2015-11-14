import unittest
import lab8

class TestQueue(unittest.TestCase):
    def stackQueue_push(self):
        queue = lab8.StackQueue()
        queue.push(3)
        queue.push(5)
        queue.push(7)
        result = queue.pop()
        expected = 3
        self.assertEqual(result, expected)

    def stackQueue_empty(self):
        queue = lab8.StackQueue()
        result = queue.pop()
        expected = None
        self.assertEqual(result, expected)

    def stackQueue_size(self):
        queue = lab8.StackQueue()
        queue.push(3)
        queue.push(5)
        queue.push(7)
        result = queue.size()
        expected = 3
        self.assertEqual(result, expected)

    def MaxQueue_max(self):
        max_queue = lab8.MaxElementQueue()
        max_queue.push(2)
        max_queue.push(9)
        max_queue.push(4)
        max_queue.push(10)
        result = max_queue.max_elem()
        expected = 10
        self.assertEqual(expected, result)

    def MaxQueue_max_pop(self):
        max_queue = lab8.MaxElementQueue()
        max_queue.push(2)
        max_queue.push(9)
        max_queue.push(4)
        max_queue.push(10)
        max_queue.pop()
        result = max_queue.max_elem()
        expected = 9
        self.assertEqual(result, expected)

    def MaxQueue_empty(self):
        max_queue = lab8.MaxElementQueue()
        result = max_queue.max_elem()
        expected = None
        self.assertEqual(result, expected)
