import copy
from typing import Generic, Iterable, TypeVar, Optional

#from Trees.src.trees.bst_tree import BST


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
        self.left: Optional[Iterable["BSTNode[T]"]] = None
        self.right: Optional[Iterable["BSTNode[T]"]] = None
        self.parent = parent
        self.children = children
        if self.children is not None:
            self._update_children(children)
        self._num_children = 0 
        # self.num_of_children = 0
        # if self.children:
        #     self.left = next(self.children)
        #     self.right = next(self.children)
        # else:
        #     self.left = None
        #     self.right = None

    def _update_children(self, children_iterable) -> None:
        self.left = next(children_iterable)
        self._num_children += 1
        self.right = next(children_iterable)
        self._num_children += 1

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

# node = BSTNode(10, iter((BSTNode(5), BSTNode(12))))
# >>> node = BSTNode(10, iter((BSTNode(5), BSTNode(12))))
# >>> node.value
# 10
# >>> node.left
# <__main__.BSTNode object at 0x10385ac70>
# >>> tup = (BSTNode(5), BSTNode(12))
# >>> node = BSTNode(10, iter(tup))
# >>> node.value
# 10
# >>> node.left
# <__main__.BSTNode object at 0x10385a5e0>
# >>> node.left.value
# 5
# >>> node.right
# <__main__.BSTNode object at 0x10385a760>
# >>> node.right.value
# 12
# >>> for n in iter(node):
# ...     print(n)
# ... 
# <__main__.BSTNode object at 0x10385a5e0>
# <__main__.BSTNode object at 0x10385a760>
# >>> for n in iter(node):
# ...     print(n.value)
# ... 
# 5
# 12

root = BSTNode(10)
root.value

tup = (BSTNode(5), BSTNode(12))
node = BSTNode(root.value, iter(tup))
node = BSTNode(10, iter(tup))

node.value
node.left
node.left.value
node.right
node.right.value

for n in iter(node):
    print(n.value)



root = BSTNode(10)
left_node = BSTNode(value = 5, parent=root)
right_node = BSTNode(value = 12, parent=root)
#tup = (BSTNode(value = 5, parent = root), BSTNode(value = 12, parent = 12))
node = BSTNode(root.value, iter((left_node, right_node)))

left_node.value
left_node.parent.value

for child in iter(node):
    print('Child Nodes value:', child.value, 'Child Parent Nodes value:', child.parent.value)

child_nodes = [child.value for child in iter(node)]
child_nodes[1]