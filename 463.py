class Solution:
    def islandPerimeter(self, grid) -> int:
        ans=0
        move=[[1,0],[1,0],[0,1],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans=ans+4
                    for k in range(4):
                        if i+move[k][0]>=0 and i+move[k][0]<len(grid):
                            if j+move[k][1]>=0 and j+move[k][1]<len(grid[0]):
                                if grid[i+move[k][0]][j+move[k][1]]==1:
                                    ans=ans-1
        return ans
a= Solution()
a.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])