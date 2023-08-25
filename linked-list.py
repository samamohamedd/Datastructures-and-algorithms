class node:
    def __init__(self, value=None, n=None):
        self.value = value
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class linklist:
    def __init__(self, r=None):
        self.head = r
        self.length = 0

    #   self.tail = self.head

    def get_len(self):
        return self.length

    def addToBeggning(self, value):
        new_node = node(value, self.head)
        self.head = new_node
        self.length += 1

    def remove(self, value):
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_value() == value:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node.get_next()
                return "done"
            else:
                prev_node = this_node
                this_node = prev_node.get_next()
        return "not found"

    def insert(self , i , value):
        new_node = node(value)
        index = 0
        prev_node = None
        if self.head is None:
            self.head = new_node
        else:
            this_node = self.head
            while this_node.next_node:
                if index == i :
                    if prev_node:
                        prev_node.set_next(new_node)
                    new_node.set_next(this_node)
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
        llist =""
        while itr:
            llist += str(itr.value) + " --> "
            itr = itr.next_node
        print(llist)

mylist = linklist()
mylist.addToBeggning(5)
mylist.append(4)
mylist.append(6)
mylist.append(88)
mylist.append(9)
mylist.remove(10)
mylist.print()
mylist.insert(3,65)
mylist.insert(1,44)
mylist.print()
