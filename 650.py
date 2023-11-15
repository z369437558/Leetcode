class Solution:
    def minSteps(self, n: int) -> int:
        dp=[[999999 for i in range(n+1)]for j in range(n+1)]
        dp[1][0]=0
        dp[1][1]=1
        for i in range(2,n+1):
            for j in range(1,i):
                if i%2==0 and i//2==j:
                    dp[i][j]=min(dp[i-j][j]+1,min(dp[i//2])+2)
                else:
                    dp[i][j]=dp[i-j][j]+1
        return min(dp[n])
a =Solution()
print(a.minSteps(6))