class Solution:
    def queensAttacktheKing(self, queens: list[list[int]], king: list[int]) -> list[list[int]]:
        move=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        def bfs(x,y):
            for i in range(8):
                for j in range(8):
                    if x+move[i][0]*j in range(8) and y+move[i][1]*j in range(8) and [x+move[0][i]*j,y+move[1][i]*j] in queens:
                        ans.append([x+move[i][0]*j,y+move[i][1]*j])
                        break
        ans=[]
        bfs(king[0],king[1])
        return ans
a = Solution()
a.queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0])