from AVL import insert_avl_tree
from twothreetree import insert_23_tree
from utils import print_23_tree

if __name__ == '__main__':
    data = [2, 10, 5, 9, 6, 4, 1, 1.5, 1.6, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6]
    # root = insert_avl_tree(data)
    root = insert_23_tree(data)
