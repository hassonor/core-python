class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        """Search for a node with the given target value."""
        if self.data == target:
            print("Found it!")
            return self
        elif self.left and self.data > target:
            return self.left.search(target)
        elif self.right and self.data < target:
            return self.right.search(target)
        print("Value is not in the tree")

    def calc_height(self, height=0):
        """Calculate the height of the tree."""
        left_height = self.left.calc_height(height + 1) if self.left else height
        right_height = self.right.calc_height(height + 1) if self.right else height
        return max(left_height, right_height)

    def traverse_pre_order(self):
        """Pre-order traversal of the tree."""
        print(self.data)
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()

    def traverse_in_order(self):
        """In-order traversal of the tree."""
        if self.left:
            self.left.traverse_in_order()
        print(self.data)
        if self.right:
            self.right.traverse_in_order()

    def traverse_post_order(self):
        """Post-order traversal of the tree."""
        if self.left:
            self.left.traverse_post_order()
        if self.right:
            self.right.traverse_post_order()
        print(self.data)


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        """Search for a node with the given target value."""
        return self.root.search(target)

    def calc_height(self):
        """Calculate the height of the tree."""
        return self.root.calc_height()

    def traverse_pre_order(self):
        """Pre-order traversal of the tree."""
        self.root.traverse_pre_order()

    def traverse_in_order(self):
        """In-order traversal of the tree."""
        self.root.traverse_in_order()

    def traverse_post_order(self):
        """Post-order traversal of the tree."""
        self.root.traverse_post_order()


tree = Tree(Node(50), 'Tree Traversals')
# Constructing the tree
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)
tree.root.left.left.left.left = Node(2)

print("Traverse Pre-Order")
tree.traverse_pre_order()

print("\nTraverse In-Order")
tree.traverse_in_order()

print("\nTraverse Post-Order")
tree.traverse_post_order()

print(tree.calc_height())

# Drawing of the tree:
#          50
#        /    \
#      25      75
#     /  \
#   10    35
#  /  \   /  \
# 5   13 30  42
# /
# 2

tree_2 = Tree(Node(50), 'Short Tree')
print(tree_2.calc_height())
