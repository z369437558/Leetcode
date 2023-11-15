class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root) -> int:
        def check(list1):
            t=0
            for i in list1:
                if i%2!=0:
                    t+=1
                if t>=2:
                    return False
            return True
        def dfs(root):
            if root.left:
                list1[root.left.val]+=1
                dfs(root.left)
                list1[root.left.val]-=1
            if root.right:
                list1[root.right.val]+=1
                dfs(root.right)
                list1[root.right.val]-=1
            if not root.left and not root.right:
                if check(list1):
                    self.ans+=1
        self.ans=0
        list1 = [0 for i in range(10)]
        list1[root.val]=1
        dfs(root)
        return self.ans 
a = Solution()
root = TreeNode(2)
root.left = TreeNode(3)
root. right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right=TreeNode(1)
print(a.pseudoPalindromicPaths(root))                     