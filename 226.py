
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if root is None:
            return root
        if root.left is not None and root.right is not None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left,root.right = root.right,root.left
        else:
            if root.left is None and root.right is not None:
                self.invertTree(root.right)
                root.left,root.right = root.right,root.left
                return root
            if root.left is not None and root.right is None:
                self.invertTree(root.left)
                root.left,root.right = root.right,root.left
                return root
            if root.left is None and root.right is None:
                return root
        return root
a = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
a.invertTree(root)