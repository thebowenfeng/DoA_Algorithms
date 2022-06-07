from utils import print_tree, DELIMITER


class Node:
    def __init__(self, value=None):
        self.value = value
        self.b_factor = None
        self.left = None
        self.right = None


def get_height(node):
    '''
    Gets height of a subtree
    :param node:
    :return:
    '''
    if node is None:
        return 0
    else:
        return max(get_height(node.left), get_height(node.right)) + 1


def get_b_factor(node):
    '''
    Recursively construct balance factor of all nodes in a tree
    :param node:
    :return:
    '''
    # No children node
    if node.left is None and node.right is None:
        node.b_factor = 0
    elif node.right is None:
        get_b_factor(node.left)
        node.b_factor = get_height(node.left)
    elif node.left is None:
        get_b_factor(node.right)
        node.b_factor = -get_height(node.right)
    else:
        get_b_factor(node.left)
        get_b_factor(node.right)
        node.b_factor = get_height(node.left) - get_height(node.right)


def recursive_insert(node, value, queue):
    if value < node.value:
        queue.append("left")
        if node.left is None:
            node.left = Node(value)
        else:
            recursive_insert(node.left, value, queue)
    else:
        queue.append("right")
        if node.right is None:
            node.right = Node(value)
        else:
            recursive_insert(node.right, value, queue)

    if len(queue) > 2:
        queue.pop(0)


def ll_rotation(node):
    # Special case
    if node.left.right is not None:
        print("Left left rotation (SPECIAL CASE) used for node: " + str(node.value))
        prev_left_right = node.left.right
        new_root = node.left

        node.left.right = node

        node.left = prev_left_right

        return new_root
    else:
        print("Left left rotation used for node: " + str(node.value))
        node.left.right = node

        new_root = node.left
        node.left = None
        return new_root


def lr_rotation(node):
    print("Left right rotation used for node: " + str(node.value))
    old_left = node.left
    node.left = old_left.right
    node.left.left = old_left
    old_left.right = None

    new_root = node.left
    new_root.right = node
    node.left = None

    return new_root


def rr_rotation(node):
    if node.right.left is not None:
        print("Right right rotation (SPECIAL CASE) used for node: " + str(node.value))
        prev_right_left = node.right.left
        new_root = node.right

        new_root.left = node
        node.right = None
        node.right = prev_right_left

        return new_root
    else:
        print("Right right rotation used for node: " + str(node.value))
        new_root = node.right
        new_root.left = node
        node.right = None
        return new_root


def rl_rotation(node):
    print("Right left rotation used for node: " + str(node.value))
    old_right = node.right
    node.right = old_right.left
    node.right.right = old_right
    old_right.left = None

    new_root = node.right
    new_root.left = node
    node.right = None

    return new_root


def fix_tree(node, case):
    if case == "ll":
        # Check if left subtree is imbalanced
        if get_height(node.left) > 2 and node.left.b_factor < -1 or node.left.b_factor > 1:
            node.left = fix_tree(node.left, "ll")

            return node
        else:
            return ll_rotation(node)
    elif case == "lr":
        # Check if left subtree is imbalanced
        if get_height(node.left) > 2 and node.left.b_factor < -1 or node.left.b_factor > 1:
            node.left = fix_tree(node.left, "lr")

            return node
        else:
            return lr_rotation(node)
    elif case == "rr":
        # Check if right subtree is imbalanced
        if get_height(node.right) > 2 and node.right.b_factor < -1 or node.right.b_factor > 1:
            node.right = fix_tree(node.right, "rr")

            return node
        else:
            return rr_rotation(node)
    elif case == "rl":
        # Check if right subtree is imbalanced
        if get_height(node.right) > 2 and node.right.b_factor < -1 or node.right.b_factor > 1:
            node.right = fix_tree(node.right, "rl")

            return node
        else:
            return rl_rotation(node)
    else:
        raise Exception("Invalid imbalance case")


def insert(node, value):
    print(f"Inserting {value}...")
    queue = []

    if node is None:
        print(f"First insertion, created a new node")
        print(DELIMITER)
        return Node(value)
    else:
        recursive_insert(node, value, queue)
        # print_tree(node, val="value")
        get_b_factor(node)

        # Tree is imbalanced
        if node.b_factor < -1 or node.b_factor > 1:
            print("Tree looks like this currently. This tree requires rebalancing:")
            print_tree(node, val="value")
            print(f"Here are the balance factors of the tree")
            print_tree(node, val="b_factor")
            # Left-left imbalance
            if queue[0] == "left" and queue[1] == "left":
                new_root = fix_tree(node, "ll")
            elif queue[0] == "left" and queue[1] == "right":
                # Left-right imbalance
                new_root = fix_tree(node, "lr")
            elif queue[0] == "right" and queue[1] == "right":
                # Right-right imbalance
                new_root = fix_tree(node, "rr")
            elif queue[0] == "right" and queue[1] == "left":
                # Right-left imbalance
                new_root = fix_tree(node, "rl")
            else:
                raise Exception("Invalid imbalance case")

            print("Tree after rebalancing:")
            print_tree(new_root, val="value")
            print(DELIMITER)
            return new_root
        else:
            print("Tree is balanced")
            print_tree(node, val="value")
            print(DELIMITER)
            return node


def insert_avl_tree(array):
    '''
    Inserts an array of values into an AVL tree.
    :param array: Array of (preferably) integers, but can handle any arbitrary data type
    :return: None
    '''
    root = None
    for value in array:
        root = insert(root, value)

    return root
