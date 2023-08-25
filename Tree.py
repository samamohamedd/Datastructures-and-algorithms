class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.children = [] #each element is an instance of anouther tree 

    def add_child (self, child):
        child.parent = self
        self.children.append(child)

    def get_levels(self):
        level = 0
        p = self.parent
        while p :
            level +=1
            p = p.parent
        return level     

    def print_tree(self):
        spaces = '  ' * self.get_levels() 
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_animal_tree():
    root = TreeNode('Animals')
    cats = TreeNode('cats')
    cats.add_child(TreeNode('meme'))
    cats.add_child(TreeNode('soso'))
    cats.add_child(TreeNode('lolo'))
    
    dogs = TreeNode('dogs')
    dogs.add_child(TreeNode('hoho'))
    dogs.add_child(TreeNode('rere'))


    root.add_child(cats)
    root.add_child(dogs)

    return root

if __name__ == '__main__':
    root = build_animal_tree()     
    root.print_tree()
    pass