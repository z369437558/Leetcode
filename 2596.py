class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        n=len(grid)
        position=[(-1,-1) for i in range(n*n)]
        for i in range(n):
            for j in range(n):
                position[grid[i][j]]=(i,j)
        for i in range(1,n*n):
            if not (abs(position[i][0]-position[i-1][0])==2 and abs(position[i][1]-position[i-1][1])==1 or  abs(position[i][1]-position[i-1][1])==2 and abs(position[i][0]-position[i-1][0])==1):
                return False
            if position[i]==(-1,-1):
                return False
        return True
a = Solution()
print(a.checkValidGrid([[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]))