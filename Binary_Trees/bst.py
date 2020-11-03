import random


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def getChildren(self):
        children = []
        if (self.left != None):
            children.append(self.left.value)
        if (self.right != None):
            children.append(self.right.value)
        return children


class BST:

    def __init__(self):
        self.root = None

    def setRoot(self, curr_node):
        self.root = curr_node
        print("Root Inserted", curr_node.value)

    def insertNode(self, root_node, curr_node):

        if curr_node.value <= root_node.value:
            if root_node.left is None:
                root_node.left = curr_node

            else:
                self.insertNode(root_node.left, curr_node)


        elif curr_node.value > root_node.value:
            if root_node.right is None:
                root_node.right = curr_node
            else:
                self.insertNode(root_node.right, curr_node)

    def insert(self, val):

        node = Node(val)

        if self.root is None:
            self.setRoot(node)
        else:
            self.insertNode(self.root, node)

    def inorder(self, root_node, values):

        if root_node:
            self.inorder(root_node.left, values)
            values.append(root_node.value)
            self.inorder(root_node.right, values)

        return values

    def preorder(self, root_node, values):

        if root_node:
            values.append(root_node.value)
            self.inorder(root_node.left, values)
            self.inorder(root_node.right, values)

        return values

    def postorder(self, root_node, values):

        if root_node:
            self.inorder(root_node.left, values)
            values.append(root_node.value)
            self.inorder(root_node.right, values)
            values.append(root_node.value)

        return values


tree = BST()
len = 10

for i in range(len):
    tree.insert(random.randint(1, 50))

inorder, preorder, postorder = [],[],[]
print(tree.inorder(tree.root, inorder))

print(tree.preorder(tree.root, preorder))
print(tree.postorder(tree.root, postorder))
