import queue
class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        ans=0
        b=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
        moves = [[0,1],[0,-1],[-1,0],[1,0]]
        def bfs(x,y):
            q=queue.Queue()
            q.put((x,y))
            b[x][y]=1
            tot=0
            while q.qsize()>0:
                x1,y1=q.get()
                tot+=grid[x1][y1]
                for move in moves:
                    if x1+move[0] in range(len(grid)) and y1+move[1] in range(len(grid[0])) and b[x1+move[0]][y1+move[1]]==0 and grid[x1+move[0]][y1+move[1]]!=0:
                        q.put((x1+move[0],y1+move[1]))
                        b[x1+move[0]][y1+move[1]]=1
            return tot
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0 and b[i][j]==0:
                    ans = max(ans,bfs(i,j))
        return ans
        
a = Solution()
print(a.findMaxFish(grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))