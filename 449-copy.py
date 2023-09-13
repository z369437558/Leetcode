def f(root):
    if root is None:
        return
    self.list1.append(root.val)
    if root.left is not None:
        f(root.left)
    if root.right is not None:
        f(root.right)
    