from collections import Counter
class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        class node:
            def __init__(self,val,index):
                self.val=val
                self.index = index
                self.sonlist=[]
                self.c=Counter(val)
        def dp(root):
            for son in root.sonlist:
                dp(son)
                root.c=root.c+son.c
            ans[root.index]=root.c[root.val]
        nodelist=[]
        ans=[0 for i in range(n)]
        set1 = set()
        set1.add(0)
        for i in range(n):
            nodelist.append(node(labels[i],i))
        for i in range(len(edges)):
            if edges[i][0] in set1:
                nodelist[edges[i][0]].sonlist.append(nodelist[edges[i][1]])
            else:
                nodelist[edges[i][1]].sonlist.append(nodelist[edges[i][0]])
            set1.add(edges[i][0])
            set1.add(edges[i][1])
        dp(nodelist[0])
        return ans
a = Solution()
print(a.countSubTrees(n = 4, edges = [[0,2],[0,3],[1,2]], labels = "aeed"))