class Solution:
    def largestLocal(self, grid):
        n = len(grid)
        ans = [[0] *(n-2)] *(n-2)
        for i in range(n-2):
            for j in range(n-2):
                print(grid[j][i:i+3])
                print(grid[j+1][i:i+3])
                print(grid[j+2][i:i+3])
                ans[i][j]=max(max(grid[j][i:i+3]),max(grid[j+1][i:i+3]),max(grid[j+2][i:i+3]))
        return ans
a = Solution()
a.largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])