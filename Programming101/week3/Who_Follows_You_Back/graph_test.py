import unittest
from graph import DirectedGraph


class DirectedGraphTests(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_add_edge_non_existing_nodes(self):
        self.graph.add_edge("Ionko", "Dingo")
        self.assertEqual(self.graph.nodes, {"Ionko": ["Dingo"], "Dingo": []})

    def test_add_edge_only_one_existing_node(self):
        self.graph.add_edge("Ionko", "Dingo")
        self.graph.add_edge("Dingo", "Penka")
        self.assertEqual(self.graph.nodes,
                         {"Ionko": ["Dingo"], "Dingo": ["Penka"], "Penka": []})

    def test_add_edge_existing_nodes(self):
        self.graph.add_edge("Ionko", "Dingo")
        self.graph.add_edge("Dingo", "Ionko")
        self.assertEqual(self.graph.nodes,
                         {"Ionko": ["Dingo"], "Dingo": ["Ionko"]})

    def test_get_neighbours_for_existing_nodes(self):
        self.graph.add_edge("Ionko", "Dingo")
        self.assertEqual(self.graph.get_neighbours_for("Ionko"),
                         ["Dingo"])

    def test_get_neighbours_for_non_existing_nodes(self):
        self.assertEqual(self.graph.get_neighbours_for("ASDF"), [])

    def test_path_between_direct_neighbours(self):
        self.graph.add_edge("Ionko", "Dingo")
        self.assertTrue(self.graph.path_between("Ionko", "Dingo"))
        self.assertFalse(self.graph.path_between("Dingo", "Ionko"))

    def test_path_between_cyclic_neighbours(self):
        self.graph.add_edge("1", "2")
        self.graph.add_edge("2", "3")
        self.graph.add_edge("2", "4")
        self.graph.add_edge("4", "5")
        self.graph.add_edge("4", "6")

        self.graph.add_edge("3", "2")

        self.assertTrue(self.graph.path_between("2", "6"))
        self.assertFalse(self.graph.path_between("6", "2"))

    def test_path_between_indirect_neighbours(self):
        self.graph.add_edge("1", "2")
        self.graph.add_edge("2", "3")
        self.graph.add_edge("2", "4")
        self.graph.add_edge("4", "5")
        self.graph.add_edge("4", "6")

        self.assertTrue(self.graph.path_between("1", "6"))
        self.assertFalse(self.graph.path_between("6", "5"))


if __name__ == '__main__':
    unittest.main()
