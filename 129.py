class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        ans=[0]
        def dfs(root,s):
            s+=str(root.val)
            if root.left:
                dfs(root.left,s)
            if root.right:
                dfs(root.right,s)
            if not root.left and not root.right:
                ans[0]+=int(s)
        dfs(root,'')
        return ans[0]
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
a = Solution()
print(a.sumNumbers(root))