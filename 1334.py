class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        dis = [[99999999 for i in range(n)] for i in range(n)]
        for i in range(n):
            dis[i][i]=0
        tot= [0 for i in range(n)]
        for edge in edges:
            dis[edge[0]][edge[1]]=edge[2]
            dis[edge[1]][edge[0]]=edge[2]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
        ans = 0
        min1 = 99999999
        for i in range(n):
            for j in range(n):
                if dis[i][j]<=distanceThreshold:
                    tot[i]+=1
            if tot[i]<=min1:
                min1= tot[i]
                ans = i
        return ans
a = Solution()
print(a.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))