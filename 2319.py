class Solution:
    def checkXMatrix(self, grid) -> bool:
        n=len(grid)
        for i in range(n):
            for j in range(n):
                print(i == j,i+j+1==n,grid[i][j]==0)
                print(i != j,i+j+1!=n,grid[i][j]!=0)
                if ((i == j or i+j+1==n) and grid[i][j]==0) or  ((i != j or i+j+1!=n) and grid[i][j]!=0):
                    return False
        return True
a=Solution()
a.checkXMatrix(grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])