class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = newnode

    def print_list(self):
        temp = self.head
        if temp is None:
            print("no elements in the list")
        while temp:
            print(temp.data)
            temp = temp.next

    def prepend(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None

    def reverse_l(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def insert_atpos(self, prev_node, data):
        if not prev_node:
            print("the given element does not exist!!")
            return

        newnode = Node(data)

        cur_node = self.head
        newnode.next = prev_node.next
        prev_node.next = newnode

    def removedup(self):
        cur = self.head
        prev = None
        my_dict = {}

        while cur:
            if cur.data in my_dict:
                prev.next = cur.next
                cur = None
            else:
                my_dict[cur.data] = 1
                prev = cur
            cur = prev.next

    def merge_sort(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            newhead = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = newhead
        return self.head
