# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.distancedict = {}
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root):
            if root.left:
                dfs(root.left)
                for k,v in root.left.distancedict.items():
                    if k in root.distancedict:
                        root.distancedict[k]+=v
                    else:
                        root.distancedict[k]=v
            if root.right:
                dfs(root.right)
                for k,v in root.right.distancedict.items():
                    if k in root.distancedict:
                        root.distancedict[k]+=v
                    else:
                        root.distancedict[k]=v
            if not root.left and not root.right:
                root.distancedict[0]=1
            if root.left and root.right:
                for item1 in root.left.distancedict.items():
                    for item2 in root.right.distancedict.items():
                        if item1[0]+item2[0]<=distance:
                            ans[0]+=item1[1]*item2[1]
        TreeNode.distancedict ={}
        ans =[0]
        dfs(root)
        return ans[0]


a = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print(a.countPairs(root,3))