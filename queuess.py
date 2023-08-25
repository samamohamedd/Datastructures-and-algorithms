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


class queue:
    first = None
    last = None
    length = 0

    def enqueue(self, data):
        
        new_node = node(data)
        if self.first == None:
            self.first = new_node
            self.last = self.first
        else:
            if self.last:
                self.last.set_next(new_node)  
                self.last = self.last.get_next()

    def dequeue(self):
         if self.first is None:
             return "it's empty"
         elif self.first is self.last:
             self.first = None
             self.last = None
         else:
            if self.first is not None:
                self.first = self.first.next_node

    def peek(self):
        if self.first:
            return self.first.data

    def print(self):
        if self.first is None:
            print("the list is empty")
        itr = self.first
        llist = ""
        while itr:
            llist += str(itr.data) + " --> "
            itr = itr.next_node
        print(llist)


myqueue = queue()
myqueue.enqueue(8)
myqueue.enqueue(5)
myqueue.enqueue(9)
myqueue.print()
myqueue.dequeue()
myqueue.print()
myqueue.dequeue()
myqueue.print()


