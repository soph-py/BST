# Your solution for the donor problem here
from typing import TypeVar
import sys
from Trees.src.trees.bst_tree import BST
from Trees.src.donor_prog.donor import Donor

T = TypeVar('T')
K = TypeVar('K')

def create_tree(path: str) -> BST[T, K]:
    tree = BST(key = lambda x: x)
    #abs_path = 'TreeProblem/Trees/src/donor_prog/donor_files/' + relative_path
    with open(path) as file:
        count_nodes = 0
        for line in file:
            id_, amt = line.split(sep = ':')
            id_ = int(id_)
            amt = int(amt)
            donor_object = Donor(id_, amt)
            tree.add_value(donor_object.node.value)
            count_nodes += 1
    tree._num_nodes = count_nodes
    return tree

def parse_commands(tree , args):
    args_list = ['all', 'rich', 'cheap', 'who']
    if args == args_list[0]:
        return all_(tree)
    elif args == args_list[1]:
        return rich(tree)
    elif args == args_list[2]:
        return cheap(tree)
    else:
        who_amount = sys.argv[3]
        return who_args(tree, str(who_amount))

def all_(tree):
    ...

def rich(tree):
    max_node = tree.get_max_node()
    return f'{max_node.id_} with a donation of {max_node.value}'

def cheap(tree):
    min_node = tree.get_min_node()
    return f'{min_node.id_} with a donation of {min_node.value}'

def who_args(tree, amt: str):
    if '+' in amt:
        ## for node in tree.root:
            ## if node <= amt:
                # return f'{node.id_} with a donation of {node.value}'
        ...
    elif '-' in amt:
        ...
    else: # if who arg is passed without additional args
        value = int(amt)
        get_donor_node = tree.get_node(value)
        return f'{get_donor_node.id_} with a donation of {get_donor_node.value}'

def main():
    donor_tree = create_tree(sys.argv[1])
    parse_commands(donor_tree, sys.argv[2])

if __name__ == '__main__':
    main()



## making sure the donor class creates a node object
# d = Donor(0, 120)
# d.node.value

## we need to traverse the down the root node (postorder traversal?) and somehow sort the values of the nodes
## to print them in order of least amount to greatest 
t = create_tree('TreeProblem/Trees/src/donor_prog/donor_files/donor10.txt')
t.root.value
t.root.left.value
t.__len__()
t._num_nodes
t.root.left.value
t.inorder_traversal()