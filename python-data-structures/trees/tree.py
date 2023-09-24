class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self
        elif self.left and self.data > target:
            return self.left.search(target)
        elif self.right and self.data < target:
            return self.right.search(target)

        print("Values is not in the tree")


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)


node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(100)

my_tree = Tree(node, 'Hasson\'s Tree')

found = my_tree.search(100)
print(found.data if found and found.data else "No Value Found")
