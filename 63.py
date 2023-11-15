class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        def f(x,y):
            if x==0 or y==-0:
                return 0
            if x==1 and y==1:
                return 1
            if obstacleGrid[x-1][y-1]==1:
                return 0

            return f(x-1,y)+f(x,y-1)
        return f(len(obstacleGrid),len(obstacleGrid[0]))
a = Solution()
print(a.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))