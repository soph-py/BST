from typing import TypeVar
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')


class Donor(object):
    """
    Maybe it would be a good idea to a make a simple donor class
    """
    def __init__(self, id_: K, value: T):
        self.id_ = id_
        self.value = value
        self.node = BSTNode(value = value, id_ = id_)

    def __repr__(self):
        id_ = str(self.id_)
        amt = str(self.value)
        return f'{id_} with a donation of {amt}'