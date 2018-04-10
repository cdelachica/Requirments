class TreeNode:
    def __init__(self, head, val, leftchild = None, rightchild = None, parents = None):
        self.head = head
        self.payload = val
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.parents = parents

    def hasLeftchild(self):
        return self.leftchild

    def hasRightchild(self):
        return self.rightchild

    def isLeftchild(self):
        return self.parents and self.parents.leftchild == self

    def isRightchild(self):
        return self.parents and self.parents.rightchild == self

    def isRoot(self):
        return not self.parents

    def isleaf(self):
        return not (self.rightchild or self.leftchild)

    def hasanychildren(self):
        return self.rightchild and self.leftchild

    def hasbothchildren(self):
        return self.rightchild and self.leftchild

    def replacenodedata(self, head, val,ltcd,rtcd):
        self.head = head
        self.payload = val
        self.leftchild = ltcd
        self.rightchild = rtcd
        if self.hasLeftchild():
            self.leftchild.parents = self
        if self.hasRightchild():
            self.rightchild.parents = self