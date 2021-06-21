class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right

    def __str__(self):
        print(self.data),
        if self.left:
            self.left.__str__()
        if self.right:
            self.right.__str__()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



