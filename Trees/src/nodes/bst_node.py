import copy
from typing import Generic, Iterable, TypeVar, Optional

#from Trees.src.trees.bst_tree import BST


T = TypeVar('T')
K = TypeVar('K')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: gert the right child
    """
    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None, id_: Optional[K] = None) -> None:
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        self.value = value
        self.id_ = id_
        self.left = None
        self.right = None
        self.children = children
        if self.children is not None:
            self.left = next(self.children)
            self.right = next(self.children)

    # def _update_children(self, children_iterable) -> None:
    #     self.left = next(children_iterable)
    #     self.right = next(children_iterable)

    def count_children(self) -> int:
        if self.left is None and self.right is None:
            return self._count_cur_node_children
        elif self.left and self.right is None:
            return 1 # has 1 left child 
        elif self.right and self.left is None:
            return 1
        else: # if self.left and self.right are not none, node has 2 children
            return 2

    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right


    def __deepcopy__(self, memodict) -> "BSTNode[T]":
        """
        I noticed that for some tests deepcopying didn't
        work correctly until I implemented this method so here
        it is for you
        :param memodict:
        :return:
        """
        copy_node = BSTNode(copy.deepcopy(self.value, memodict))
        copy_node.left = copy.deepcopy(self.left, memodict)
        copy_node.right = copy.deepcopy(self.right, memodict)
        return copy_node

# root = BSTNode(10)
# root.value

# tup = (BSTNode(5), BSTNode(12))
# node = BSTNode(root.value, iter(tup))
# node = BSTNode(10, iter(tup))

# node.value
# node.left
# node.left.value
# node.right
# node.right.value

# for n in iter(node):
#     print(n.value)