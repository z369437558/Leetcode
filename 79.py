from collections import Counter
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        flag = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        move=[[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(x,y,p):
            if p==len(word)-1:
                return True 
            f = False
            for i in range(4):
                if x+move[i][0] in range(len(board)) and y+move[i][1] in range(len(board[0])) and board[x+move[i][0]][y+move[i][1]]==word[p+1] and flag[x+move[i][0]][y+move[i][1]]==0:
                    flag[x+move[i][0]][y+move[i][1]]=1
                    f = f or bfs(x+move[i][0],y+move[i][1],p+1)
                    flag[x+move[i][0]][y+move[i][1]]=0
            return f
        list1 = [board[i][j] for i in range(len(board)) for j in range(len(board[0]))]
        c = Counter(list1)
        c1 = Counter(list(word))
        if c1<=c:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==word[0]:
                        flag[i][j]=1
                        if bfs(i,j,0):
                            return True
                        flag[i][j]=0
        return False
a = Solution()
a.exist([["A","A","A"],["A","a","a"],["A","a","A"],["a","a","A"]],"AAAAAA")

["A","B","C","E"]
["S","F","E","S"]
["A","D","E","E"]