from tree_utils import print_tree, DELIMITER


class Node:
    def __init__(self, value, data=None):
        self.data = data
        self.value = value
        self.display_val = None
        self.left = None
        self.right = None

        if data is not None:
            self.display_val = f"{value} ({data})"
        else:
            self.display_val = str(value)

    def __str__(self):
        return self.display_val

    def __lt__(self, other):
        if self.data is not None and other.data is not None and self.value == other.value:
            if not self.data.isalnum() and other.data.isalnum():
                return True
            elif self.data.isalnum() and not other.data.isalnum():
                return False
            return self.data > other.data
        else:
            return self.value < other.value


def find_data(node: Node, encoding: dict, path: str):
    if node.left is None and node.right is None:
        encoding[node.data] = path
    else:
        find_data(node.left, encoding, path + "0")
        find_data(node.right, encoding, path + "1")


def huffman(message: str):
    freq = {}
    for char in message:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    nodes = []
    for key, val in freq.items():
        nodes.append(Node(val, key))

    nodes.sort()

    print("Performing huffman encoding. The following characters are in the message alongside its frequencies:")
    print(freq)

    while len(nodes) > 1:
        print(DELIMITER)
        node1 = min(nodes)
        node2 = None
        for node in nodes:
            if node != node1 and (node2 is None or node < node2):
                node2 = node

        node1_ind = nodes.index(node1)
        node2_ind = nodes.index(node2)

        # Swap
        if node1_ind > node2_ind:
            temp = node1
            node1 = node2
            node2 = temp

        print("Selecting the following two smallest nodes to combine: {} and {}".format(node1, node2))

        new_node = Node(node1.value + node2.value, None)
        new_node.left = node1
        new_node.right = node2
        nodes.insert(node1_ind, new_node)

        print("The new tree looks like this:")
        print_tree(new_node, val="display_val")

        nodes.remove(node1)
        nodes.remove(node2)

    print("Huffman tree is complete. The tree looks like:")
    print_tree(nodes[0], val="display_val")

    root_node = nodes[0]
    encoding = {}
    find_data(root_node, encoding, "")

    print("The encodings based on the tree is: {}".format(encoding))
    encoded_msg = ""
    for char in message:
        encoded_msg += encoding[char]

    print("The encoded message is: {}".format(' '.join([i for i in encoded_msg])))

    return encoded_msg, encoding


def huffman_decode(encoded_msg: str, encodings: dict):
    print("Performing huffman decoding on the following message: {}".format(encoded_msg))
    print("Following encoding is used: {}".format(encodings))
    decoded_msg = ""
    flipped_encodings = {v: k for k, v in encodings.items()}

    curr_chunk = ""
    for bit in encoded_msg:
        curr_chunk += bit
        if curr_chunk in flipped_encodings:
            decoded_msg += flipped_encodings[curr_chunk]
            curr_chunk = ""

    print("Decoded message: {}".format(decoded_msg))
    return decoded_msg


