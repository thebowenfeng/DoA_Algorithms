from tree_utils import print_tree, DELIMITER


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


def recursive_insert(node, value):
    if value < node.value:
        if node.left is None:
            node.left = Node(value)
        else:
            recursive_insert(node.left, value)
    else:
        if node.right is None:
            node.right = Node(value)
        else:
            recursive_insert(node.right, value)


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


def fix_tree(parent, node):
    if node is None:
        return None

    lowest = [0]
    lowest_node = [None]
    lowest_parent = [None]

    def dfs(par: tuple, nod: Node, lvl, low: list, low_par: list, low_num: list):
        if nod is None:
            return
        else:
            if abs(nod.b_factor) > 1 and lvl > low_num[0]:
                low[0] = nod
                low_num[0] = lvl
                low_par[0] = par

            dfs((nod, "left"), nod.left, lvl + 1, low, low_par, low_num)
            dfs((nod, "right"), nod.right, lvl + 1, low, low_par, low_num)

    dfs(None, node, 1, lowest_node, lowest_parent, lowest)
    lowest_node = lowest_node[0]
    lowest_parent = lowest_parent[0]

    if lowest_node.left is not None and lowest_node.left.left is not None:
        case = "ll"
    elif lowest_node.right is not None and lowest_node.right.right is not None:
        case = "rr"
    elif lowest_node.right is not None and lowest_node.right.left is not None:
        case = "rl"
    elif lowest_node.left is not None and lowest_node.left.right is not None:
        case = "lr"
    else:
        raise Exception("Invalid imbalance case")

    if case == "ll":
        if lowest_parent is None:
            return ll_rotation(lowest_node)
        else:
            # node is left child of parent
            if lowest_parent[1] == "left":
                lowest_parent[0].left = ll_rotation(lowest_node)
            else:
                lowest_parent[0].right = ll_rotation(lowest_node)
    elif case == "lr":
        if lowest_parent is None:
            return lr_rotation(lowest_node)
        else:
            # node is left child of parent
            if lowest_parent[1] == "left":
                lowest_parent[0].left = lr_rotation(lowest_node)
            else:
                lowest_parent[0].right = lr_rotation(lowest_node)
    elif case == "rr":
        if lowest_parent is None:
            return rr_rotation(lowest_node)
        else:
            # node is left child of parent
            if lowest_parent[1] == "left":
                lowest_parent[0].left = rr_rotation(lowest_node)
            else:
                lowest_parent[0].right = rr_rotation(lowest_node)
    elif case == "rl":
        if lowest_parent is None:
            return rl_rotation(lowest_node)
        else:
            # node is left child of parent
            if lowest_parent[1] == "left":
                lowest_parent[0].left = rl_rotation(lowest_node)
            else:
                lowest_parent[0].right = rl_rotation(lowest_node)
    else:
        raise Exception("Invalid imbalance case")


def insert(node, value):
    def check_imbalance(node):
        if node is None:
            return False

        if node.b_factor < -1 or node.b_factor > 1:
            return True
        else:
            return check_imbalance(node.left) or check_imbalance(node.right)

    print(f"Inserting {value}...")
    queue = []

    if node is None:
        print(f"First insertion, created a new node")
        print(DELIMITER)
        return Node(value)
    else:
        recursive_insert(node, value)
        # print_tree(node, val="value")
        get_b_factor(node)

        # Tree is imbalanced
        if check_imbalance(node):
            print("Tree looks like this currently. This tree requires rebalancing:")
            print_tree(node, val="value")
            print(f"Here are the balance factors of the tree")
            print_tree(node, val="b_factor")
            # Left-left imbalance
            new_root = fix_tree(None, node)

            if new_root is not None:
                print("Tree after rebalancing:")
                print_tree(new_root, val="value")
                print(DELIMITER)
                return new_root
            else:
                print("Tree after rebalancing:")
                print_tree(node, val="value")
                print(DELIMITER)
                return node
        else:
            print("Tree is balanced")
            print_tree(node, val="value")
            print(DELIMITER)
            return node


def get_max(node):
    if node is None:
        return float('-inf')

    return max(node.value, get_max(node.left), get_max(node.right))


def recursive_delete(parent, node, value):
    if node.value == value:
        # Leaf node, no children
        if node.left is None and node.right is None:
            if parent is not None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                # Deleting root node
                node.value = None
        elif node.left is None and node.right is not None:
            if parent is None:
                node.value = node.right.value
                node.right = None
            else:
                parent.right = node.right
        elif node.left is not None and node.right is None:
            if parent is None:
                node.value = node.left.value
                node.left = None
            else:
                parent.left = node.left
        else:
            left_max = get_max(node.left)
            node.value = left_max
            recursive_delete(node, node.left, left_max)
    else:
        if node.left is not None:
            recursive_delete(node, node.left, value)

        if node.right is not None:
            recursive_delete(node, node.right, value)


def delete(node, value):
    print(f"Deleting {value}...")

    def detect_case(node):
        if node is None:
            return False

        if node.b_factor < -1 or node.b_factor > 1:
            # Detect which case it is
            if node.left is not None and node.left.left is not None:
                return "ll"
            elif node.right is not None and node.right.right is not None:
                return "rr"
            elif node.left is not None and node.left.right is not None:
                return "lr"
            elif node.right is not None and node.right.left is not None:
                return "rl"
            else:
                raise Exception("Error detecting imbalance case for deletion")
        else:
            return detect_case(node.left) or detect_case(node.right)

    recursive_delete(None, node, value)

    # Check if root is not None (tree is empty)
    if node.value is not None:
        get_b_factor(node)

        case = detect_case(node)
        if not case:
            print("Tree is still balanced after deletion balanced")
            print_tree(node, val="value")
            print(DELIMITER)
            return node
        else:
            print("Tree is imbalanced after deletion. It is a {} imbalance case. Tree is like this: ".format(case))
            print_tree(node, val="value")
            print("Fixing tree...")

            new_root = fix_tree(None, node, case)

            print("Tree fixed. Tree is like this:")
            print_tree(node, val="value")
            print(DELIMITER)

            if new_root is not None:
                return new_root
            else:
                return node
    else:
        return None


def insert_avl_tree(array, node=None):
    '''
    Inserts an array of values into an AVL tree.
    :param array: Array of (preferably) integers, but can handle any arbitrary data type
    :return: Root node of the AVL tree
    '''
    root = node
    for value in array:
        root = insert(root, value)

    return root


def delete_avl_tree(root, array):
    '''
    Deletes an array of values from an AVL tree.
    :param root: Root node of the tree
    :param array: Array of (preferably) integers, but can handle any arbitrary data type
    :return: Root node of the AVL tree
    '''
    for value in array:
        root = delete(root, value)

    return root
