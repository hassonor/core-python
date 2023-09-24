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

    def get_nodes_at_depth(self, depth, nodes=[]):
        """Get all nodes at a specific depth in the tree."""
        if depth == 0:
            nodes.append(self.data)
            return nodes
        if self.left:
            self.left.get_nodes_at_depth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))
        if self.right:
            self.right.get_nodes_at_depth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))
        return nodes

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

    def get_nodes_at_depth(self, depth):
        """Get all nodes at a specific depth in the tree."""
        return self.root.get_nodes_at_depth(depth)

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

    def _node_to_char(self, n, spacing):
        if n is None:
            return '_' + (' ' * spacing)
        spacing = spacing - len(str(n)) + 1
        return str(n) + (' ' * spacing)

    def print(self, label=''):
        print(self.name + ' ' + label)
        height = self.root.calc_height()
        spacing = 3
        width = int((2 ** height - 1) * (spacing + 1) + 1)
        # Root offset
        offset = int((width - 1) / 2)
        for depth in range(0, height + 1):
            if depth > 0:
                # print directional lines
                print(' ' * (offset + 1) + (' ' * (spacing + 2)).join(
                    ['/' + (' ' * (spacing - 2)) + '\\'] * (2 ** (depth - 1))))
            row = self.root.get_nodes_at_depth(depth, [])
            print((' ' * offset) + ''.join([self._node_to_char(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset / 2) - 1
        print('')


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

tree_2 = Tree(Node(50), 'Short Tree')
print(tree_2.calc_height())

tree_3 = Tree(Node(50), 'Get all nodes at depth')
# Constructing tree_3
tree_3.root.left = Node(25)
tree_3.root.right = Node(75)
tree_3.root.left.left = Node(13)
tree_3.root.left.right = Node(35)
tree_3.root.left.right.right = Node(37)
tree_3.root.right.left = Node(55)
tree_3.root.right.right = Node(103)
tree_3.root.left.left.left = Node(2)
tree_3.root.left.left.right = Node(20)
tree_3.root.right.right.right = Node(256)

print(tree_3.get_nodes_at_depth(3))
tree_3.print()
# Drawing of tree_3:
#          50
#        /    \
#      25      75
#     /  \    /  \
#   13    35 55  103
#  /  \     \       \
# 2   20    37     256
