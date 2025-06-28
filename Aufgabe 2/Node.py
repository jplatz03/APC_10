class Node:
    def __innit__(self, value):
        self.value = value
        self.left=None
        self.right=None

    def add(self, val):
        if val>self.value:
         if self.right is None:
            self.right=Node(val)
         else:
             self.right.add(val)
        else:
            if self.left is None:
                self.left=Node(val)
            else:
                self.left.add(val)
    def get(self, value):
        if self.value==value:
            return self
        elif self.value<value and self.left:
            return self.left.get(value)
        elif self.value>value and self.right:
            return self.right.get(value)
        else:
            return None

    def remove(self, val, parent=None):
        if val < self.value:
            if self.left:
                return self.left.remove(val, self)
        elif val > self.value:
            if self.right:
                return self.right.remove(val, self)
        else:
            if self.left and self.right:
                successor = self.right.find_min()
                self.value = successor.value
                self.right.remove(successor.value, self)
            elif parent is None:
                return self
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
            return self

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.value, end=' ')
        if self.right:
            self.right.print_inorder()