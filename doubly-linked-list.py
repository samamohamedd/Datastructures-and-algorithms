class node:
    def __init__(self, value=None, n=None, p=None):
        self.value = value
        self.next_node = n
        self.prev_node = p

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_prev(self):
        return self.prev_node

    def set_prev(self, p):
        self.prev_node = p


class linklist:
    def __init__(self, h=None, t=None):
        self.head = h
        self.length = 0
        self.tail = t

    def get_len(self):
        return self.length

    def append2(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        elif self.tail is not None:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = node(value, self.head)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        elif self.head is not None:
            self.head.set_prev(new_node)
            self.head = new_node
            self.length += 1

    def remove(self, value):
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_value() == value:
                if prev_node:
                    if this_node.next_node:
                        prev_node.set_next(this_node.get_next())
                        this_node.next_node.set_prev(prev_node)
                    else:
                        if self.tail:
                            if self.tail.prev_node:
                                self.tail.prev_node.set_next(None)
                else:
                    self.head = this_node.get_next()
                return "done"

            else:
                prev_node = this_node
                this_node = prev_node.get_next()
        return "not found"

    def insert(self, i, value):
        new_node = node(value)
        index = 0
        prev_node = None
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            this_node = self.head
            while this_node.next_node:
                if index == i:
                    if prev_node:
                        prev_node.set_next(new_node)
                    new_node.set_next(this_node)
                    this_node.set_prev(new_node)
                    new_node.set_prev(prev_node)
                    self.length += 1
                    break
                else:
                    prev_node = this_node
                    this_node = this_node.next_node
                    index += 1

    def find(self, value):
        this_node = self.head
        while this_node:
            if this_node.get_value() == value:
                return f"{value} is found"
            else:
                this_node = this_node.get_next()
        return f"{value} not found"

    def append(self, value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
        else:
            this_node = self.head
            while this_node.next_node:
                this_node = this_node.next_node
            this_node.next_node = new_node

    def print(self):
        if self.head is None:
            print("the list is empty")
        itr = self.head
        llist = ""
        while itr:
            llist += str(itr.value) + " --> "
            itr = itr.next_node
        print(llist)


mylist = linklist()
mylist.append2(4)
mylist.append2(6)
mylist.append2(88)
mylist.append2(9)
mylist.prepend(7)
mylist.insert(3, 77)
mylist.insert(1, 90)
print(mylist.find(55))
mylist.remove(88)
mylist.remove(9)
mylist.print()
