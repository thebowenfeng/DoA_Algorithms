from AVL import insert_avl_tree, delete_avl_tree
from twothreetree import insert_23_tree

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,9,10,11]
    root = insert_avl_tree(data)

    to_delete = [5,6,7,8,9,10,11]
    root = delete_avl_tree(root, to_delete)

    #root = insert_23_tree(data)

