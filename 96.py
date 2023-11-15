class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
class Solution:
    def numTrees(self, n: int) -> int:
        ans = [0]
        flag=[0 for i in range(n+1)]
        def dfs(root,l,r):
            if sum(flag)==n:
                ans[0]+=1
            for i in range(l,r+1):
                if flag[i]==0:
                    if i<root.val:
                        root.left=Node(i)
                        flag[i]=1
                        dfs(root.left,l,root.val-1)
                        flag[i]=0
                        root.left=None
                    else:
                        root.right=Node(i)
                        flag[i]=1
                        dfs(root.right,root.val+1,r)
                        flag[i]=0
                        root.right=None
        for i in range(1,n+1):
            flag[i]=1
            dfs(Node(i),1,n)
            flag[i]=0
        return ans[0]
a = Solution()
a.numTrees(3)