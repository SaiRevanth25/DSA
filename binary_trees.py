from queue import Queue

class BinarySearch:
    class Node:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.data = val

    def __init__(self):
        self.node_count = 0
        self.root = None

    def compared(self, n1, n2):
        if n1 < n2:
            return -1
        elif n1 > n2:
            return 1
        else:
            return 0

    def add(self, node, elem):
        if node is None:
            return self.Node(elem)
        else:
            if self.compared(elem, node.data) < 0:
                node.left = self.add(node.left, elem)
            else:
                node.right = self.add(node.right, elem)
        return node

    def contains(self, node, elem):
        if node is None:
            return False

        cmp = self.compared(elem, node.data)

        if cmp < 0:
            return self.contains(node.left, elem)
        elif cmp > 0:
            return self.contains(node.right, elem)
        else:
            return True

    def find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def remove(self, node, elem):
        if node is None:
            return None

        cmp = self.compared(elem, node.data)

        if cmp < 0:
            node.left = self.remove(node.left, elem)
        elif cmp > 0:
            node.right = self.remove(node.right, elem)

        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.find_max(node.left)
                node.data = temp.data
                node.left = self.remove(node.left, temp.data)

        return node

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.preorder(node.left)
        self.preorder(node.right)
        print(node.data, end=" ")

    def _level_order(self):
        if self.root is None:
            return

        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            print(node.data, end=" ")

            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)

    def level_order(self):
        self._level_order()
        print()



    def size(self):
        return self.node_count

    def is_empty(self):
        return self.size() == 0

    def contain(self, elem):
        return self.contains(self.root, elem)

    def append(self, elem):
        if self.contain(elem):
            return False
        self.root = self.add(self.root, elem)
        self.node_count += 1
        return True

    def remove_elem(self, elem):
        if self.contain(elem):
            self.root = self.remove(self.root, elem)
            self.node_count -= 1
            return True
        return False

    def height(self):
        return self.height(self.root)

    def pre_order(self):
        self.preorder(self.root)
        print()

    def post_order(self):
        self.postorder(self.root)
        print()

    def in_order(self):
        self.inorder(self.root)
        print()
