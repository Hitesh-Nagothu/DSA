class AVLTreeNode:

    def __init__(self, key, val=None, skew=0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
        self.skew = skew

class AVLTree:

    def __init__(self):
        self.root = None

    def util_insert(self, root, key, val=None):
        if root is None:
            new_node = AVLTreeNode(key, val, skew=0)
            print("Inserted Root", new_node.key)
            return new_node

        if key < root.key:
            # Insert recursively to left subtree
            left_node = self.util_insert(root.left, key, val)
            left_node.parent = root
            root.left = left_node
            print("Inserted", left_node.key)

        elif key > root.key:
            # Insert recursively to right subtree
            right_node = self.util_insert(root.right, key, val)
            right_node.parent = root
            root.right = right_node

        # if key==root.val, do not insert into the tree to avoid duplications
        else:
            return root

        # Updates to be done after inserting a new node
        if root.left is not None:
            left_height = root.left.height
        else:
            left_height = 0

        if root.right is not None:
            right_height = root.right.height
        else:
            right_height = 0

        root.height = max(self.height(root.left), self.height(root.right)) +1
        root.skew = self.height(root.left)-self.height(root.right)

        #rebalance=self.rebalance(root)
        #print("rebalanced",rebalance.key)
        return self.rebalance(root)

    def insert(self, key, val=None):
        self.root = self.util_insert(self.root, key, val)

    def height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def rotate_right(self, node):
        print("Rebalacing activated")
        beta_root = node.left
        temp = beta_root.right

        beta_root.right = node
        beta_root.parent = node.parent
        node.parent = beta_root

        node.left = temp

        if temp is not None:
            temp.parent = node

        if beta_root.parent:
            if beta_root.parent.left == node:  # call was on left subtree
                beta_root.parent.left = beta_root
            else:
                beta_root.parent.right = beta_root

        # Since node position is changed, update its height

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        node.skew = self.height(node.left) - self.height(node.right)

        beta_root.height = max(self.height(beta_root.left), self.height(beta_root.right)) + 1
        beta_root.skew = self.height(beta_root.left) - self.height(beta_root.right)

        return beta_root

    def rotate_left(self, node):
        print("LEft Rebalancing activated")

        beta_root=node.right
        temp=beta_root.left

        node.parent=beta_root
        beta_root.left=node
        beta_root.parent=node.parent

        node.right=temp

        if temp is not None:
            temp.parent=node

        if beta_root.parent:
            if beta_root.parent.left == node:
                beta_root.parent.left=beta_root
            else:
                beta_root.parent.right=beta_root

        node.height=max(self.height(node.left), self.height(node.right))+1
        node.skew=self.height(node.left) - self.height(node.right)

        beta_root.height=max(self.height(beta_root.left), self.height(beta_root.right))+1
        beta_root.skew=self.height(beta_root.left)-self.height(beta_root.right)

        return beta_root


    def rebalance(self, root):

        if root.skew ==2 :
            if root.left.skew > 0:
                # Left Left Imbalance
                return self.rotate_right(root)

            elif root.left.skew < 0:
                # Left Right Imbalance
                self.rotate_left(root.left)
                return self.rotate_right(root)

        elif root.skew ==-2:

            if root.right.skew > 0:
                # Right Left Imbalance
                self.rotate_right(root.right)
                return self.rotate_left(root)
            elif root.right.skew < 0:
                # Right Right Imbalance
                return self.rotate_left(root)

        else:
            return root




test = AVLTree()

test.insert(50)
test.insert(17)
test.insert(76)
test.insert(9)
test.insert(23)
test.insert(54)
test.insert(14)
test.insert(19)
test.insert(72)
test.insert(12)
test.insert(67)


print(test.root.key)
print(test.root.right.key)
print(test.root.left.skew)
print(test.root.right.skew)