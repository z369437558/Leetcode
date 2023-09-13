class Solution:
    def countServers(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if sum(grid[i])>1:
                for j in range(n):
                    if grid[i][j]==1:
                        ans[i][j]=1
        for j in range(n):
            if sum(row[j] for row in grid)>1:
                for i in range(m):
                    if grid[i][j]==1:
                        ans[i][j]=1
        return sum(map(sum,ans))
a = Solution()
a.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])