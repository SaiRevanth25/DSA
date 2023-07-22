class AVLTreeRecursive:
    class Node:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.value = val
            self.bf = 0
            self.height = 0

    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def compared(self, i, j):
        if i < j:
            return -1
        elif i > j:
            return 1
        return 0

    def insert(self, node, val):
        if node is None:
            return AVLTreeRecursive.Node(val)

        cmp = self.compared(val, node.value)
        if cmp < 0:
            new_left_node = self.insert(node.left, val)
            if new_left_node is None:
                return None
            node.left = new_left_node
        elif cmp > 0:
            new_right_node = self.insert(node.right, val)
            if new_right_node is None:
                return None
            node.right = new_right_node
        else:
            return None

        self.update(node)
        return self.balance(node)

    def update(self, node):
        left_node_height = node.left.height if node.left else -1
        right_node_height = node.right.height if node.right else -1
        node.height = 1 + max(left_node_height, right_node_height)
        node.bf = right_node_height - left_node_height

    def balance(self, node):
        if node.bf == -2:
            if node.left.bf <= 0:
                return self.left_left_case(node)
            else:
                return self.left_right_case(node)
        elif node.bf == 2:
            if node.right.bf >= 0:
                return self.right_right_case(node)
            else:
                return self.right_left_case(node)
        return node

    def left_left_case(self, node):
        return self.right_rotation(node)

    def left_right_case(self, node):
        node.left = self.left_rotation(node.left)
        return self.right_rotation(node)

    def right_right_case(self, node):
        return self.left_rotation(node)

    def right_left_case(self, node):
        node.right = self.right_rotation(node.right)
        return self.left_rotation(node)

    def left_rotation(self, node):
        new_parent = node.right
        node.right = new_parent.left
        new_parent.left = node
        self.update(node)
        self.update(new_parent)
        return new_parent

    def right_rotation(self, node):
        new_parent = node.left
        node.left = new_parent.right
        new_parent.right = node
        self.update(node)
        self.update(new_parent)
        return new_parent

    def find_min(self, node):
        while node.left:
            node = node.left
        return node.value

    def find_max(self, node):
        while node.right:
            node = node.right
        return node.value

    def remove(self, node, val):
        if node is None:
            return None

        cmp = self.compared(val, node.value)
        if cmp < 0:
            node.left = self.remove(node.left, val)
        elif cmp > 0:
            node.right = self.remove(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.find_min(node.right)
                node.value = temp
                node.right = self.remove(node.right, temp)

        self.update(node)
        return self.balance(node)

    def height(self):
        if self.root is None:
            return 0
        return self.root.height

    def size(self):
        return self.nodeCount

    def is_empty(self):
        return self.size() == 0

    def contains(self, value):
        node = self.root
        while node:
            cmp = self.compared(value, node.value)
            if cmp < 0:
                node = node.left
            elif cmp > 0:
                node = node.right
            else:
                return True
        return False

    def insert_value(self, value):
        new_root = self.insert(self.root, value)
        if new_root is not None:
            self.nodeCount += 1
            self.root = new_root
        return new_root is not None

    def remove_value(self, value):
        new_root = self.remove(self.root, value)
        if new_root is None:
            return False
        self.root = new_root
        self.nodeCount -= 1
        return True

    def level_order(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
