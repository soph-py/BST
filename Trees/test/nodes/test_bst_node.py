import unittest
from Trees.src.nodes import bst_node


class TestBSTNode(unittest.TestCase):

    def test_value(self):
        node_test = bst_node.BSTNode(10)
        self.assertEqual(node_test.value, 10)

    def test_left_child(self):
        node_test = bst_node.BSTNode(10)
        node_test.left = bst_node.BSTNode(5)
        self.assertEqual(node_test.left.value, 5)

    def test_right_child(self):
        node_test = bst_node.BSTNode(10)
        node_test.right = bst_node.BSTNode(12)
        self.assertEqual(node_test.right.value, 12)

    def test_two_children(self):
        root_node = bst_node.BSTNode(10)
        child_nodes = (bst_node.BSTNode(5), bst_node.BSTNode(12))
        node = bst_node.BSTNode(root_node.value, iter(child_nodes))
        root_node_value_expected = 10
        left_child_value_expected = 5
        right_child_value_expected = 12
        self.assertEqual(node.value, root_node_value_expected)
        self.assertEqual(node.left.value, left_child_value_expected)
        self.assertEqual(node.right.value, right_child_value_expected)

    def test_parent(self):
        root_node = bst_node.BSTNode(10)
        child_nodes = (bst_node.BSTNode(value = 5, parent = root_node), bst_node.BSTNode(value = 12, parent = root_node))
        node = bst_node.BSTNode(root_node, iter(child_nodes))

        left_parent_expected = 10
        self.assertEqual(child_nodes[0].parent.value, left_parent_expected)
        right_parent_expected = 10
        self.assertEqual(child_nodes[1].parent.value, right_parent_expected)
        root_nodes_children_expected = [5, 12]
        root_nodes_children_actual = [child.value for child in iter(node)]

        # left child node value
        self.assertEqual(root_nodes_children_actual[0], root_nodes_children_expected[0])
        # right child node value
        self.assertEqual(root_nodes_children_actual[1], root_nodes_children_expected[1])

    def test_iter(self):
        ...

if __name__ == '__main__':
    unittest.main()
