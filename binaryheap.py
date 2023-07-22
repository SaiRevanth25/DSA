class BinaryHeap():
    def __init__(self, elems=None):
        if elems is None:
            elems = []
            self.heap = []
            self.size = 0
            if isinstance(elems, (list, tuple)):
                for elem in elems:
                    self.add(elem)
            else:
                print("wrong choice!!")

    def is_empty(self):
        return  self.size == 0

    def clear(self):
        self.heap.clear()
        self.size = 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.heap[0]

    def contains(self, key):
        return key in self.heap

    def add(self,elem):
        if elem is None:
            raise ValueError
        self.heap.append(elem)
        self.size += 1
        self.heap_up(self.size - 1)

    def remove(self, elem):
        if elem is None:
            raise ValueError
        for i in range(self.size):
            if self.heap[i] == elem:
                self.remove_at(i)
                return True
            return False

    def remove_at(self, index):
        if 0 <= index < self.size:
            removed_elem = self.heap[index]
            last_elem = self.heap[self.size - 1]
            self.heap[index] = last_elem
            self.size -= 1
            self.heap_down(index)
            return removed_elem
        return None

    def swap(self, p, q):
        self.heap[p], self.heap[q] = self.heap[q], self.heap[p]

    def heap_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def heap_down(self, index):
        while True:
            left = 2*index + 1
            right = 2*index + 2
            smallest = left
            if right < self.size and self.heap[right] < self.heap[left]:
                smallest = right
            if left >= self.size or self.heap[index] < self.heap[smallest]:
                break
            self.swap(index, smallest)
            index = smallest

    def is_min_heap(self, index=0):
        if index >= self.size:
            return True
        left = 2*index + 1
        right = 2*index + 2
        if left < self.size and self.heap[index] > self.heap[left]:
            return False
        if right < self.size and self.heap[index] > self.heap[right]:
            return False
        return self.is_min_heap(left) and self.is_min_heap(right)
