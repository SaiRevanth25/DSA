class FenwickTree:
    def __init__(self, sz_or_val):

        if isinstance(sz_or_val, int):
            self.N = sz_or_val + 1
            self.tree = [0] * self.N

        elif isinstance(sz_or_val, list):
            if sz_or_val is None:
                raise ValueError("values in list cannot be None!!")

            self.N = len(sz_or_val)
            self.tree = [0] + sz_or_val[:]

            for i in range(1, self.N):
                parent = i + self._lsb(i)
                if parent < self.N:
                    self.tree[parent] += self.tree[i]

        else:
            raise ValueError("invalid input type")

    def _lsb(self, i):
        return i & -i

    def prefix_sum(self, i):
        total_sum = 0
        while i != 0:
            total_sum += self.tree[i]
            i &= ~self._lsb(i)
        return total_sum

    def sum_range(self, left, right):
        if right < left:
            raise ValueError("make sure left <= right")
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def get(self, i):
        return self.sum_range(i, i)

    def add(self, i, v):
        while i < self.N:
            self.tree[i] += v
            i += self._lsb(i)

    def set(self, i, v):
        self.add(i, v - self.get(i))

    def __str__(self):
        return str(self.tree[1:])


if __name__ == "__main__":
    fenwick = FenwickTree(5)
    print(fenwick)
    fenwick.add(1, 2)
    fenwick.add(2, 3)
    fenwick.add(3, 5)
    fenwick.add(4, 1)
    print(fenwick)
    print(fenwick.sum_range(2, 4))
    fenwick.set(3, 7)
    print(fenwick)
