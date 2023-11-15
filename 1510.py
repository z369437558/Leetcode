class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp=[False for i in range(n+1)]
        dp[0]=False
        dp[1]=True
        dp[2]=False
        for i in range(3,n+1):
            flag=False
            for j in range(1,i+1):
                if j*j>i:
                    break
                flag=flag or not dp[i-j*j] 
            dp[i]=flag
        return dp[n]
a = Solution()
print(a.winnerSquareGame(4))