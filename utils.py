DELIMITER = "==============================================="

def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


def print_23_tree(root):
    # BFS search
    queue = [(root, 0)]
    curr_level_nodes = []
    prev_level = 0
    all_nodes = []
    outer_is_all_none = False

    while queue:
        node, level = queue.pop(0)

        if level > prev_level:
            prev_level = level
            is_all_none = True
            for naode in curr_level_nodes:
                if naode != "None":
                    is_all_none = False
                    break

            if is_all_none:
                outer_is_all_none = True
                break
            else:
                all_nodes.append(curr_level_nodes)
                curr_level_nodes = [str(node)]
        else:
            curr_level_nodes.append(str(node))

        if node is not None:
            queue.append((node.child1, level+1))
            queue.append((node.child2, level+1))
            queue.append((node.child3, level+1))
        else:
            queue.append((None, level+1))
            queue.append((None, level + 1))
            queue.append((None, level + 1))

    if not outer_is_all_none:
        all_nodes.append(curr_level_nodes)

    level_str = []
    NODE_WIDTH = 8
    gap = 1
    pg = 0
    #Print
    for level in range(len(all_nodes), 0, -1):
        nodes = all_nodes[level-1]
        curr_str = " " * pg

        for i in range(3 ** (level - 1)):
            # Just print node
            if i == 3 ** level - 1:
                if nodes[i] != "None":
                    curr_str += str(nodes[i])
                else:
                    curr_str += " " * NODE_WIDTH
            else:
                if nodes[i] != "None":
                    curr_str += str(nodes[i]) + " " * gap
                else:
                    curr_str += " " * (NODE_WIDTH + gap)

        curr_str += " " * pg
        level_str.append(curr_str)
        pg = pg + NODE_WIDTH + gap
        gap = 3 * gap + 2 * NODE_WIDTH

    for i in range(len(level_str) - 1, -1, -1):
        print(level_str[i])
        print(" " * (len(level_str[i]) - 1))
