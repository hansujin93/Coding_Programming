class Tree:
    def __init__(self, content, left = None, right = None):
        self.content = content
        self.left = left
        self.right = right

    def leaf(self, count=1): #default: content exists
        if self.left:
            count += self.left.leaf()
        if self.right:
            count += self.right.leaf()
        return count

def total(tree):
    if tree is None:
        return 0
    return total(tree.left) + total(tree.right) + tree.content

def avg(tree):
    if total(tree) == 0:
        return 0
    return total(tree) / tree.leaf()
