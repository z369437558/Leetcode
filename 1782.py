import numpy as np
class Solution:
    def countPairs(self, n, edges, queries):
        nodeset=set()
        node= [0 for i in range(20002)]
        ans=[0 for i in range(len(queries))]
        incident=[]
        for edge in edges:
            node[edge[0]]+=1
            node[edge[1]]+=1
            nodeset.add(edge[0])
            nodeset.add(edge[1])
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                incident.append(node[i]+node[j])
                if [i,j] in edges:
                    incident[-1]-=edges.count([i,j])
                if [j,i] in edges:
                    incident[-1]-=edges.count([j,i])
        incident.sort()
        for i,querie in enumerate(queries):
            left=0
            right=len(incident)-1
            while left<right:
                mid=(left+right)//2
                if incident[mid]<=querie:
                    left = mid+1
                else:
                    right=mid
            ans[i]=len(incident)-left
            if querie>=max(incident):
                ans[i]=0

        return ans
a=Solution()
a.countPairs(8,[[2,5],[5,4],[4,3],[7,3],[5,8],[6,1],[7,5],[6,1],[7,5],[3,1],[6,4],[6,8],[6,5],[5,6],[8,1],[1,6],[1,3],[5,6],[8,3],[6,2]],[2,5,4,3,0,4,4,3,3,2,3,1,5,7,5,1,6,18,14])