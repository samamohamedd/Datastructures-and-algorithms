from collections import deque


class node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.num = 0

    def insert(self, value):
        curr = self.root
        if self.num == 0:
            self.root = node(value)
            self.num += 1
        else:
            new_node = node(value)
            while curr:
                if curr.value == new_node.value:
                    break
                elif curr.value > new_node.value:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = new_node
                        curr = curr.left
                        self.num += 1
                elif curr.value < new_node.value:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = new_node
                        curr = curr.right
                        self.num += 1

    def lookup(self, value):
        curr = self.root
        while curr:
            if curr.value == value:
                print(f"{value} is found")
                break
            elif curr.value > value:
                if curr.left:
                    curr = curr.left
                else:
                    print(f"{value} is not found")
                    break
            elif curr.value < value:
                if curr.right:
                    curr = curr.right
                else:
                    print(f"{value} is not found")
                    break

    def remove(self, value):
        curr = self.root
        parent = None
        while curr:
            if value < curr.value:
                parent = curr
                curr = curr.left

            elif value > curr.value:
                parent = curr
                curr = curr.right

            elif curr.value == value:
                # when there is no right
                if curr.right is None:
                    if parent:
                        if curr.value > parent.value:
                            parent.right = curr.left
                            break
                        elif curr.value < parent.value:
                            parent.left = curr.left
                            break
                    else:
                        self.root = curr.left

                else:  # if there is right we don't want to lose the left
                    l = curr.left
                    if curr.right.left is None:  # if the right child doesn't have left
                        if parent is None:
                            self.root = curr.left
                        else:
                            if curr.value > parent.value:
                                parent.right = curr.left
                                break
                            if curr.value < parent.value:
                                parent.left = curr.left
                                break
                    elif parent:  # if the right child have lefts
                        parent.right = curr.right
                        curr.right.left = l
                        break

    def BreadthFirstSearch(self):
        curr = self.root
        answer = []
        queue: deque = deque()
        queue.append(curr)

        while len(queue) > 0:
            curr = queue.popleft()
            answer.append(curr.value)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
        return answer

    def BreadthFirstSearchR(self, queue, ans):
        if len(queue) == 0:
            return ans
        curr = queue.pop(0)
        ans.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        return self.BreadthFirstSearchR(queue, ans)

    def DepthFirstSearchIN(self):
        return self.TraversalIN(self.root, [])

    def DepthFirstSearchPRE(self):
        return self.TraversalPRE(self.root, [])

    def DepthFirstSearchPOST(self):
        return self.TraversalPOST(self.root, [])

    def TraversalIN(self, node, arr):
        if node.left:
            self.TraversalIN(node.left, arr)
        arr.append(node.value)
        if node.right:
            self.TraversalIN(node.right, arr)
        return arr

    def TraversalPRE(self, node, arr):
        arr.append(node.value)
        if node.left:
            self.TraversalIN(node.left, arr)
        if node.right:
            self.TraversalIN(node.right, arr)
        return arr

    def TraversalPOST(self, node, arr):
        if node.left:
            self.TraversalIN(node.left, arr)
        if node.right:
            self.TraversalIN(node.right, arr)
        arr.append(node.value)
        return arr


tree = BinaryTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(15)
tree.insert(90)

# tree.BreadthFirstSearch()
# print(tree.BreadthFirstSearchR([tree.root], []))

print(tree.DepthFirstSearchPOST())

tree.remove(4)
tree.lookup(4)
tree.lookup(8)
tree.lookup(15)
tree.lookup(3)
