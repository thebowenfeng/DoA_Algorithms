from utils import print_23_tree, DELIMITER


class Node:
    def __init__(self):
        self.value1 = None
        self.value2 = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.parent = None

        # Temp storage for values
        self.temp_mid = None

        # Temp storage for children
        self.temp_left_small = None
        self.temp_left_big = None
        self.temp_right_small = None
        self.temp_right_big = None

    def __str__(self):
        if self.temp_mid is not None:
            return f"[{self.value1},{self.temp_mid},{self.value2}]"
        else:
            return f"[{self.value1},{self.value2}]"


def recursive_insert(node: Node, value):
    # Smaller than first value
    if value < node.value1:
        if node.child1 is not None:
            recursive_insert(node.child1, value)
        else:
            # Second value is empty
            if node.value2 is None:
                node.value2 = node.value1
                node.value1 = value
            else:
                # Insert value at the front, push value1 into middle
                node.temp_mid = node.value1
                node.value1 = value
    else:
        # No second value
        if node.value2 is None:
            if node.child3 is not None:
                recursive_insert(node.child3, value)
            else:
                node.value2 = value
        else:
            # Situated in the middle of 2 values
            if value < node.value2:
                if node.child2 is not None:
                    recursive_insert(node.child2, value)
                else:
                    node.temp_mid = value
            else:
                if node.child3 is not None:
                    recursive_insert(node.child3, value)
                else:
                    node.temp_mid = node.value2
                    node.value2 = value


def reconfigure_children(node: Node):
    node1 = Node()
    node2 = Node()
    if node.child1 is not None and node.child1.temp_mid is not None:
        node1.value1 = node.child1.value1
        node2.value1 = node.child1.value2

        node.temp_left_small = node1
        node.temp_left_big = node2

        node.temp_right_small = node.child2
        node.temp_right_big = node.child3
        node.child1 = None
    elif node.child2 is not None and node.child2.temp_mid is not None:
        node1.value1 = node.child2.value1
        node2.value1 = node.child2.value2

        node.temp_left_small = node.child1

        node.temp_left_big = node1
        node.temp_right_small = node2

        node.temp_right_big = node.child3
        node.child2 = None
    elif node.child3 is not None and node.child3.temp_mid is not None:
        node1.value1 = node.child3.value1
        node2.value1 = node.child3.value2

        node.temp_left_small = node.child1
        node.temp_left_big = node.child2

        node.temp_right_small = node1
        node.temp_right_big = node2
        node.child3 = None


def promote(node: Node):
    print(f"Performing promotion on node {node}.")
    # No parent node
    if node.parent is None:
        print(f"This node has no parent node/must be broken. Breaking node {node}")
        new_parent = Node()
        new_parent.value1 = node.temp_mid

        new_left = Node()
        new_right = Node()
        new_left.value1 = node.value1
        new_right.value1 = node.value2

        # Needs to restructure
        if node.temp_left_small is not None \
                or node.temp_left_big is not None \
                or node.temp_right_small is not None \
                or node.temp_right_big is not None:

            print(
                f"This node {node} has 4 children due to one of its children node promoting into it. Restructuring...")
            new_left.child1 = node.temp_left_small
            new_left.child3 = node.temp_left_big
            new_right.child1 = node.temp_right_small
            new_right.child3 = node.temp_right_big

            if node.temp_left_small is not None:
                node.temp_left_small.parent = new_left
            if node.temp_left_big is not None:
                node.temp_left_big.parent = new_left
            if node.temp_right_small is not None:
                node.temp_right_small.parent = new_right
            if node.temp_right_big is not None:
                node.temp_right_big.parent = new_right

        new_parent.child1 = new_left
        new_parent.child3 = new_right
        new_left.parent = new_parent
        new_right.parent = new_parent

        if node.child1 is not None:
            new_left.child1 = node.child1
            node.child1.parent = new_left

        if node.child3 is not None:
            new_right.child3 = node.child3
            node.child3.parent = new_right

        print(f"New top node {new_parent} has been created")
        return new_parent
    else:
        print(f"Trying to promote into the parent node {node.parent}...")
        has_reconfigured = False

        # Needs to restructure
        if node.temp_left_small is not None \
                and node.temp_left_big is not None \
                and node.temp_right_small is not None \
                and node.temp_right_big is not None:

            print(
                f"This node {node} has 4 children due to one of its children node promoting into it. Restructuring...")

            # Breaking 4 children into 2 subtrees
            new_left = Node()
            new_right = Node()
            new_left.value1 = node.value1
            new_right.value1 = node.value2

            new_left.child1 = node.temp_left_small
            new_left.child3 = node.temp_left_big
            new_right.child1 = node.temp_right_small
            new_right.child3 = node.temp_right_big

            if node.temp_left_small is not None:
                node.temp_left_small.parent = new_left
            if node.temp_left_big is not None:
                node.temp_left_big.parent = new_left
            if node.temp_right_small is not None:
                node.temp_right_small.parent = new_right
            if node.temp_right_big is not None:
                node.temp_right_big.parent = new_right

            # Find out which child node current node belongs to
            if node.parent.child1 == node:
                # Has 3 children already
                if node.parent.child2 is not None:
                    node.parent.temp_left_small = new_left
                    node.parent.temp_left_big = new_right
                    node.parent.temp_right_small = node.parent.child2
                    node.parent.temp_right_big = node.parent.child3
                else:
                    node.parent.child1 = new_left
                    node.parent.child2 = new_right
            elif node.parent.child2 == node:
                node.parent.temp_left_small = node.parent.child1
                node.parent.temp_left_big = new_left
                node.parent.temp_right_small = new_right
                node.parent.temp_right_big = node.parent.child3

                new_left.parent = node.parent
                new_right.parent = node.parent
            elif node.parent.child3 == node:
                if node.parent.child2 is not None:
                    node.parent.temp_left_small = node.parent.child1
                    node.parent.temp_left_big = node.parent.child2
                    node.parent.temp_right_small = new_left
                    node.parent.temp_right_big = new_right
                else:
                    node.parent.child2 = new_left
                    node.parent.child3 = new_right

            has_reconfigured = True
            new_left.parent = node.parent
            new_right.parent = node.parent

        # Insert mid into parent
        if node.temp_mid < node.parent.value1:
            # Parent has 2 values, needs to perform promotion again
            if node.parent.value2 is not None:
                node.parent.temp_mid = node.parent.value1
                node.parent.value1 = node.temp_mid

                print(f"Promoted into parent node, resulting in: {node.parent}. Parent node now needs promotion")
                if not has_reconfigured:
                    reconfigure_children(node.parent)
                return promote(node.parent)
            else:
                node.parent.value2 = node.parent.value1
                node.parent.value1 = node.temp_mid
                print(f"Promoted into parent node, resulting in: {node.parent}")
        else:
            # Parent has 2 values, needs to perform promotion again
            if node.parent.value2 is not None:
                # In between parent's 2 values
                if node.temp_mid < node.parent.value2:
                    node.parent.temp_mid = node.temp_mid
                else:
                    node.parent.temp_mid = node.parent.value2
                    node.parent.value2 = node.temp_mid

                print(f"Promoted into parent node, resulting in: {node.parent}. Parent node now needs promotion")
                if not has_reconfigured:
                    reconfigure_children(node.parent)
                return promote(node.parent)
            else:
                node.parent.value2 = node.temp_mid
                print(f"Promoted into parent node, resulting in: {node.parent}")

        node.temp_mid = None
        node1 = Node()
        node2 = Node()
        node1.value1 = node.value1
        node2.value1 = node.value2
        node1.parent = node.parent
        node2.parent = node.parent

        #Split node into 2
        if node.parent.child1 == node:
            node.parent.child1 = node1
            node.parent.child2 = node2
        elif node.parent.child3 == node:
            node.parent.child2 = node1
            node.parent.child3 = node2


def fix_tree(node: Node):
    # Node has 3 values, needs to perform promotion
    if node.temp_mid is not None:
        print(f"{node} has become unbalanced due to insertion of {node.temp_mid}. Current tree look like this: ")
        return promote(node)
    else:
        result1 = None
        result2 = None
        result3 = None

        if node.child1 is not None:
            result1 = fix_tree(node.child1)
        if node.child2 is not None:
            result2 = fix_tree(node.child2)
        if node.child3 is not None:
            result3 = fix_tree(node.child3)

        if result1 is not None:
            return result1
        elif result2 is not None:
            return result2
        elif result3 is not None:
            return result3
        else:
            return None


def insert(node: Node, value):
    print("Inserting: " + str(value))
    if node is None:
        print(f"{value} inserted into an empty tree")
        node = Node()
        node.value1 = value
        return node
    else:
        recursive_insert(node, value)

    result = fix_tree(node)
    if result is not None:
        return result
    else:
        return node


def insert_23_tree(array):
    root = None
    for value in array:
        root = insert(root, value)
        print("Tree after insertion...")
        print_23_tree(root)
        print(DELIMITER)

    return root
