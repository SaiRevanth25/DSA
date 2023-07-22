
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        self.load_factor_threshold = 0.7

    def _hash(self, key):
        return hash(key) % self.capacity

    def max_load_factor(self):
        return self.size / self.capacity

    def insert(self, key, value):

        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            cur = self.table[index]
            while cur:
                if cur.key == key:
                    cur.value = value
                    self.size += 1
                    return
                cur = cur.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

            if self.max_load_factor() > self.load_factor_threshold:
                self.resize(self.capacity * 2)

    def resize(self, new_capacity):
        new_table = [None] * new_capacity
        for i in range(self.capacity):
            cur = self.table[i]
            while cur:
                next_node = cur.next
                index = hash(cur.key) % new_capacity
                cur.next = new_table[index]
                new_table[index] = cur
                cur = next_node
            self.table[i] = None

        self.table = new_table
        self.capacity = new_capacity

    def search(self, key):
        index = self._hash(key)

        cur = self.table[index]
        while cur:
            if cur.key == key:
                return cur.value + 1
            cur = cur.next
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)

        prev = None
        current = self.table[index]

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                    self.size -= 1
                    return
                prev = current
                current = current.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def print_table(self):
        for i in range(self.capacity):
            print(f"Index {i}: ", end="")
            cur = self.table[i]
            while cur:
                print(f"{cur.key}:{cur.value}", end=" ")
                cur = cur.next
            print()

    def get_pos(self, key):
        index = self._hash(key)
        print(f"position of the key is {index}")
