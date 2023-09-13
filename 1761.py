class Solution:
    def minTrioDegree(self, n: int, edges: list[list[int]]) -> int:
        connect=[[0 for j in range(n+1)] for i in range(n+1)]
        f=[0 for i in range(n+1)]
        for edge in edges:
            connect[min(edge)][max(edge)]=1
            f[edge[0]]+=1
            f[edge[1]]+=1
        ans = 1600000
        flag=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if connect[i][j] and connect[i][k] and connect[j][k]:
                        ans = min (ans,f[i]+f[j]+f[k]-6)
                        flag=1
        if flag==0:
            return -1
        return ans
a = Solution()
a.minTrioDegree(4,[[1,2],[4,1],[4,2]])