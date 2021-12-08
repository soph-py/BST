import copy
from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')


class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
        """
        You must have at least one member named root

        :param root: The root node of the tree if there is one.
        If you are provided a root node don't forget to count how many nodes are in it
        :param key: The function to be applied to a node's value for comparison purposes.
        It serves the same role as the key function in the min, max, and sorted builtin
        functions
        """
        self.root = root
        self.key = key
        self._tree_len = 0

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        # Base Case
        if self.root is None:
            return -1
        # Recurse
        else:
            return self._height(self.root)

    def _height(self, cur_node: BSTNode[T]) -> int:
        """
        Get the maximum number of levels in the tree, either right or left
        Add 1 to account for root node level
        """
        return max(self._height(cur_node.left), self._height(cur_node.right)) + 1

    def __len__(self) -> int:
        """
        :return: the number of nodes in the tree
        """
        if self.root:
            return 1
        else:
            return self._length(self.root)

    def _length(self, cur_node: BSTNode[T]) -> int:
        if cur_node.left and cur_node.right: # if node has 2 children
            return self._length(cur_node.left) + self._length(cur_node.right) + 1 # add 1 to account for root node
        elif cur_node.left and cur_node.right is None:
            return self._length(cur_node.left) + 1
        else:
            return self._length(cur_node.right) + 1

    def add_value(self, value: T) -> None:
        """
        Add value to this BST
        Duplicate values should be placed on the right
        :param value:
        :return:
        """
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._add_value(value, self.root)

    def _add_value(self, value: T, cur_node: BSTNode[T]) -> None:
        """
        Handle left, right, and duplicate cases, if root node exists
        :param value: a node in the tree
        :return:
        """
        if value < cur_node.value:
            # Base Case
            if cur_node.left is None:
                cur_node.left = BSTNode(value = value, parent = cur_node)
                self._tree_len += 1
            # Recurse
            else:
                self._add_value(value, cur_node.left)
        else:
            # Base Case
            if cur_node.right is None:
                cur_node.right = BSTNode(value = value, parent = cur_node)
                self._tree_len += 1
            # Recurse
            else:
                self._add_value(value, cur_node.right)

    def get_node(self, value: K) -> BSTNode[T]:
        """
        Get the node with the specified value
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        return self._get_node(value, self.root)

    def _get_node(self, value: T, root: BSTNode[T]) -> BSTNode[T]:
        cur_node = root
        while cur_node is not None:
            if value == cur_node.value:
                return cur_node
            elif value < cur_node.value:
                cur_node = cur_node.left
            else: # value > cur_node.value
                cur_node = cur_node.right
        return None

    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        # if root is none, we have an empty tree so raise an error
        if self.root is None:
            raise EmptyTreeError()
        # returns node with largest value to the right of the tree
        else:
            return self._get_max_node(self.root)

    def _get_max_node(self, cur_node: BSTNode[T]) -> BSTNode[T]:
        # Base Case
        if cur_node.right is None: # if node does not have a right child, return itself
            return cur_node
        else: # recurse on the right
            return self._get_max_node(cur_node.right)

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        if self.root is None:
            raise EmptyTreeError()
        else:
            return self._get_min_node(self.root)
    
    def _get_min_node(self, cur_node: BSTNode[T]) -> BSTNode[T]:
        if cur_node.left is None:
            return cur_node
        else:
            return self._get_min_node(cur_node.left)

    def remove_value(self, value: K) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
        if self.root is None:
            raise EmptyTreeError()
        else:
            self._tree_len -= 1
            self._remove_value(value, self.key)

    def _remove_value(self, value: K, key: Callable[[T], K] = lambda x: x) -> None:
        cur_node = self.root
        parent = cur_node.parent
        #parent = None
        if value != key(cur_node.value):
            raise MissingValueError()
        while cur_node is not None:
            if value == key(cur_node.value): # located the node to remove 
                if cur_node.left is None and cur_node.right is None:
                    if parent is None: # this is the root node
                        self.root = None
                    elif parent.left == cur_node:
                        parent.left = None
                    else:
                        parent.right = None
                elif cur_node.node is None:
                    if parent is None:
                        self.root = cur_node.left
                    elif parent.left == cur_node:
                        parent.left = cur_node.left
                    else:
                        parent.right = cur_node.left
                elif cur_node.left is None:
                    if parent is None:
                        self.root = cur_node.right
                    elif parent.left == cur_node:
                        parent.left = cur_node.right
                    else:
                        parent.right = cur_node.right
                else: # find successor node, left most child of right subtree
                    successor_node = cur_node.right
                    while successor_node.left is not None:
                        successor_node = successor_node.left
                        succ_data = successor_node.value
                        self._remove_value(value, successor_node.value)
                        cur_node.value = succ_data
                return
            elif key(cur_node.value) < value: # search right
                parent = cur_node
                cur_node = cur_node.right
            else:
                parent = cur_node
                cur_node = cur_node.left


                # if cur_node.right is None and cur_node.left: # if root.left is not none
                #     cur_node = cur_node.left # replace with left child
                # elif cur_node.left is None and cur_node.right:
                #     cur_node = cur_node.right # replace with right child
                # elif cur_node.left and cur_node.right: # case when node has 2 children

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       BST(self.root.left) == BST(other.root.left) and \
                       BST(self.root.right) == BST(other.root.right)
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)

    def __deepcopy__(self, memodict) -> "BST[T,K]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        new_root = copy.deepcopy(self.root, memodict)
        new_key = copy.deepcopy(self.key, memodict)
        return BST(new_root, new_key)

node = BSTNode(10)
tree = BST(node)

tree.root.value

tree.add_value(8)
tree.root.right.value
tree.get_node(8).value
