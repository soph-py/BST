import unittest
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode


class TestBST(unittest.TestCase):
    def test_create_empty_tree(self) -> None:
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)
        
    def test_create_tree(self) -> None:
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)


    def test_tree_not_eq(self) -> None:
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(92)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertNotEqual(tree, cmp_tree)

    def test_min_node(self) -> None:
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(60)
        tree.add_value(220)
        tree.add_value(45)
        tree.add_value(230)
        tree._num_nodes = 9
        tree_min_exp = 45
        tree_min_actual = tree.get_min_node()
        self.assertEqual(tree_min_exp, tree_min_actual.value)

    def test_max_node(self) -> None:
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(60)
        tree.add_value(220)
        tree.add_value(45)
        tree.add_value(230)
        tree._num_nodes = 9
        tree_max_exp = 230
        tree_max_actual = tree.get_max_node()
        self.assertEqual(tree_max_exp, tree_max_actual.value)


if __name__ == '__main__':
    unittest.main()
