

import Node
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.root.add(val)

    def getNode(self, val):
        if self.root:
            return self.root.get(val)
        return None

    def remove(self, val):
        if self.root:
            if self.root.value == val and self.root.left is None and self.root.right is None:
                self.root = None
            else:
                self.root = self.root.remove(val)

    def print(self):
        if self.root:
            self.root.print_inorder()
            print()
        else:
            print("Empty Tree")