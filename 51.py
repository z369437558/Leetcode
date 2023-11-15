class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        map1=[[0 for i in range(n)]for i in range(n)]
        ans=[]
        list1=[]
        def judge(x,y):
            for i in range(x):
                for j in range(n):
                    if map1[i][j]==1 and (abs(i-x)==abs(j-y) or y==j) :
                        return False
            return True
        def backtrack(t):
            if t==n:
                ans.append(list1.copy())
                return
            for i in range(n):
                if judge(t,i):
                    list1.append('.'*(i)+'Q'+'.'*(n-i-1))
                    map1[t][i]=1
                    backtrack(t+1)
                    map1[t][i]=0 
                    list1.pop()
        backtrack(0)
        return ans
                
a = Solution()
print(a.solveNQueens(4))