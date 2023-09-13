class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: [TreeNode]) -> int:
        list1=[root]
        depth=1
        if root is None:
            return depth
        list2=[]
        while len(list1) or len(list2):
            
            if len(list1)==0:
                list1 =list2
                list2 = []
                depth=depth+1
            now = list1.pop()
            if now.left is None and now.right is None:
                return depth
            else:
                if now.left is not None:
                    list2.append(now.left)
                if now.right is not None:
                    list2.append(now.right)
a= Solution()
root = TreeNode(3)
root.left=TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
a.minDepth(root)