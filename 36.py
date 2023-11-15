class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def judge(list1):
            checklist=[0 for _ in range(10)]
            for char in list1:
                if char!='.':
                    checklist[int(char)]+=1
                    if checklist[int(char)]>1:
                        return False
            return True
        for i in range(3):
            for j in range(3):
                list1=[]
                list1.extend(board[i*3][j*3:j*3+3])
                list1.extend(board[i*3+1][j*3:j*3+3])
                list1.extend(board[i*3+2][j*3:j*3+3])
                if judge(list1)==False:
                    return False
        for i in range(9):
            if judge(board[i])==False:
                return False
            if judge([x[i] for x in board])==False:
                return False
        return True
a= Solution()
a.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])