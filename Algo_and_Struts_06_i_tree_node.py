class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def is_left_child(self):
        return self.parent != None and self.parent.left_child is self

    def is_right_child(self):
        return self.parent != None and self.parent.right_child is self

    def is_root(self):
        return self.parent == None 

    def is_leaf(self):
        return self.right_child == None and self.left_child == None

    def has_any_child(self):
        return self.right_child != None or self.left_child != None

    def has_children(self):
        return self.right_child != None and self.left_child != None

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.right_child:
                for elem in self.right_child:
                    yield elem
