import unittest
import lab14

class TestArea(unittest.TestCase):
    def test_simple_graph(self):
        graph = lab14.Graph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_vertex(6)
        graph.add_vertex(7)
        graph.add_vertex(8)
        graph.add_vertex(9)
        graph.add_direct_link(0,2)
        graph.add_direct_link(0,4)
        graph.add_direct_link(0,6)
        graph.add_direct_link(1,9)
        graph.add_direct_link(2,3)
        graph.add_direct_link(3,4)
        graph.add_direct_link(6,7)
        graph.add_direct_link(6,8)
        result = graph.top_sort(0)
        expected = [4,3,2,7,8,6,0,9,1,5]
        self.assertEqual(result,expected)

    def test_cycle_graph(self):
        graph = lab14.Graph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_vertex(6)
        graph.add_vertex(7)
        graph.add_vertex(8)
        graph.add_vertex(9)
        graph.add_direct_link(0,2)
        graph.add_direct_link(0,4)
        graph.add_direct_link(0,6)
        graph.add_direct_link(1,9)
        graph.add_direct_link(2,3)
        graph.add_direct_link(3,4)
        graph.add_direct_link(6,7)
        graph.add_direct_link(6,8)
        graph.add_direct_link(4,0)
        result = graph.top_sort(0)
        # проверка на exit???




