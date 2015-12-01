import unittest
import lab16

class TestDijkstra(unittest.TestCase):
    def no_direct_link(self):
        graph = lab16.WeightedGraph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        result = graph.shortest_path(0, 1)
        expect = []
        self.assertEqual(result, expect)

    def no_path(self):
        graph = lab16.WeightedGraph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_direct_link(0, 1, 1)
        graph.add_direct_link(0, 2, 4)
        graph.add_direct_link(1, 2, 2)
        result = graph.shortest_path(0, 3)
        expect = []
        self.assertEqual(result, expect)

    def no_path2(self):
        graph = lab16.WeightedGraph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_vertex(5)
        graph.add_direct_link(0, 1, 1)
        graph.add_direct_link(0, 2, 4)
        graph.add_direct_link(1, 2, 2)
        graph.add_direct_link(4, 3, 3)
        graph.add_direct_link(4, 5, 1)
        graph.add_direct_link(5, 3, 1)
        result = graph.shortest_path(0, 3)
        expect = []
        self.assertEqual(result, expect)

    def example_graph(self):
        graph = lab16.WeightedGraph()
        graph.add_vertex(0)
        graph.add_vertex(1)
        graph.add_vertex(2)
        graph.add_vertex(3)
        graph.add_vertex(4)
        graph.add_direct_link(0, 1, 10)
        graph.add_direct_link(0, 2, 5)
        graph.add_direct_link(1, 3, 1)
        graph.add_direct_link(1, 2, 2)
        graph.add_direct_link(2, 1, 3)
        graph.add_direct_link(2, 4, 2)
        graph.add_direct_link(2, 3, 9)
        graph.add_direct_link(3, 4, 4)
        graph.add_direct_link(4, 3, 6)
        graph.add_direct_link(4, 0, 7)
        result = graph.shortest_path(0, 3)
        expect = [0, 2, 3, 1]
        self.assertEqual(result, expect)


