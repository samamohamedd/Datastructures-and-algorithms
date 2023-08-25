class node:
    def __init__(self, data=None, n=None):
        self.data = data
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, value):
        self.data = value


class stack:
    def __init__(self) -> None:
        self.top = None
        self.buttom = None
        self.length = 0

    def push(self, data):
        new_node = node(data)
        self.length += 1
        if self.top is None:
            self.top = new_node
            self.buttom = self.top
        else:
            this_node = self.top
            while this_node.next_node:
                this_node = this_node.next_node
            this_node.set_next(new_node)
            self.top = this_node.next_node

    def push2(self, data):
        new_node = node(data)
        self.length += 1
        if self.top is None:
            self.top = new_node
            self.buttom = self.top
        else:
            holdingpointer = self.top
            self.top = new_node
            self.top.next_node = holdingpointer

    def peek(self):
        if self.top:
            return self.top.get_data()

    def pop2(self):
        if self.top is None:
            return "it's empty"
        elif self.top == self.buttom:
            self.top = None
            self.buttom = None
            self.length -= 1
        else:
            pointer = self.top.get_next()
            self.top = pointer
            self.length -= 1

    def print(self):
        if self.top is None:
            print("the list is empty")
        itr = self.top
        llist = ""
        while itr:
            llist += str(itr.data) + " --> "
            itr = itr.next_node
        print(llist)


mystack = stack()
mystack.push2(3)
mystack.push2(44)
mystack.push2(5)
mystack.push2(33)
mystack.pop2()
mystack.pop2()
print(mystack.peek())
mystack.print()
