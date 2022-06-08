from tree_utils import DELIMITER


class HashTable:
    def __init__(self, size: int, hash_func: callable, mode: str, step_size=1):
        self.size = size
        self.table = [None for _ in range(size)]
        self.hash_func = hash_func
        if mode != "open_address" and mode != "separate_chaining":
            raise Exception("Invalid mode for hashtable. Must be either 'open_address' or 'separate_chaining'")
        self.mode = mode
        self.step_size = step_size

    def insert(self, key, val):
        print(DELIMITER)
        index = self.hash_func(key)
        print("Attempting to insert key:", key, "with hash value of:", index)

        if self.table[index] is None:
            print("Current index position is empty. Inserting key into index:", index)
            if self.mode == "separate_chaining":
                self.table[index] = [(key, val)]
            else:
                self.table[index] = (key, val)

            print("New table:", self.table)
        else:
            if self.mode == "separate_chaining":
                print(f"Separate chaining is used. Key is inserted into subarray at index {index}, at the {len(self.table[index])} position")
                self.table[index].append((key, val))
                print("New table:", self.table)
            else:
                print(f"Current index position is not empty at index {index}. Commencing open address search with step size {self.step_size}")
                index += self.step_size
                if index == self.size:
                    index = 0

                fail_count = 0
                while fail_count < self.size:
                    print(f"Attempting to find next empty index position using open addressing with step size {self.step_size}")
                    if self.table[index] is None:
                        print(f"Open addressing with step size {self.step_size} is used. Key is inserted into index {index}")
                        self.table[index] = (key, val)
                        print("New table:", self.table)
                        return

                    index += self.step_size
                    fail_count += 1

                    if index == self.size:
                        index = 0
                raise Exception("Hashtable is full")

    def lookup(self, key):
        print(DELIMITER)
        index = self.hash_func(key)
        if self.table[index] is None:
            if self.mode == "separate_chaining":
                print(f"Separate chaining is used. Index {index} is empty therefore key does not exist")
                raise Exception("Key not found")
            else:
                print(f"Current index position is empty at index {index}. Commencing open address search with step size {self.step_size}")
                index += self.step_size
                if index == self.size:
                    index = 0
                fail_count = 0

                while fail_count < self.size:
                    if self.table[index] is None:
                        print(f"Current index {index} is still null. Moving onto the next position.")
                    elif key == self.table[index][0]:
                        print(f"Key {key} was found at index {index}")
                        return self.table[index][1]
                    else:
                        print(f"Current index {index} does not contain correct key. Moving onto the next position")

                    index += self.step_size
                    if index == self.size:
                        index = 0
                    fail_count += 1

                raise Exception("Key not found")
        else:
            if self.mode == "separate_chaining":
                print(f"Separate chaining is used. Searching for key {key} at index {index}")
                for i in range(len(self.table[index])):
                    if self.table[index][i][0] == key:
                        print(f"Key {key} found at index {index} at position {i} in the subarray")
                        return self.table[index][i][1]
                    print(f"Current position {i} does not contain the key. Moving on")
                raise Exception("Key not found")
            else:
                print(f"Open addressing is used. Searching for key {key} at index {index}")
                fail_count = 0
                while fail_count < self.size:
                    if self.table[index] is None:
                        print(f"Current index {index} is null. Moving onto the next position.")
                    elif key == self.table[index][0]:
                        print(f"Key {key} found at index {index}")
                        return self.table[index][1]
                    else:
                        print(f"Current index {index} does not contain correct key. Moving onto the next position")

                    index += self.step_size
                    if index == self.size:
                        index = 0
                    fail_count += 1

                raise Exception("Key not found")
