class Union:
    def __init__(self, size):
        if size <= 0:
            raise ValueError
        self._size = size
        self.numComponents = size
        self._sz = [1] * size
        self.id = [i for i in range(size)]

    def find(self, p):
        root = p
        while root != self.id[root]:
            root = self.id[root]

        while p != root:
            next_node = self.id[p]
            self.id[p] = root
            p = next_node

        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def componentSize(self, p):
        return self._sz(self.find(p))

    @property
    def size(self):
        return self._size

    def components(self):
        return self.numComponents

    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        if root1 == root2:
            return
        if self._sz[root1] < self._sz[root2]:
            self._sz[root2] += self._sz[root1]
            self.id[root1] = root2
        else:
            self._sz[root1] += self._sz[root2]
            self.id[root2] = root1
