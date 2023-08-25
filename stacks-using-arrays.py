class stack:
    stacklist: (list) = []
    length = 0

    def push(self, data):
        self.stacklist.append(data)
        self.length += 1

    def pop(self):
        if self.stacklist == []:
            return "it's empty"
        else:
            self.stacklist.pop(self.length - 1)
            self.length -= 1

    def printitems(self):
        for item in self.stacklist:
            print(item)

    def peek(self):
        return self.stacklist[self.length - 1]


mystack = stack()
mystack.push(2)
mystack.push(5)
mystack.push(9)
mystack.pop()
print(mystack.peek())
mystack.printitems()
