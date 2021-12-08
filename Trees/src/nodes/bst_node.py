import copy
from typing import Generic, Iterable, TypeVar, Optional


T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: gert the right child
    """
    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        self.value = value
        self.left: "BSTNode[T]" = None
        self.right: "BSTNode[T]" = None
        self.parent = parent
        self.children = children
        self.num_of_children = 0
        if self.children:
            self.left.value = next(self.children)
            self.right.value = next(self.children)


    ## might just be easier to add & remove nodes in node class:
    def remove_value(self):
        ...

    def add_value(self):
        ...


    # def replace_child(self, cur_child: "BSTNode[T]", new_node: "BSTNode[T]") -> None:
    #     if cur_child:
    #         cur_child.parent = BSTNode
    #     if new_node:
    #         new_node.parent = None

    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    #def get_children(self)

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
