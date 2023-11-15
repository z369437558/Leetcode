class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp=[[0 for i in range(target+1)]for j in range(n+1)]
        for i in range(1,min(k,target)+1):
            dp[1][i]=1
        for m in range(2,n+1):
            for i in range(1,target+1):
                for j in range(1,k+1):
                    if i-j>=0:
                        dp[m][i]+=dp[m-1][i-j]
        return dp[n][target]%(10**9+7)
a = Solution()
print(a.numRollsToTarget(n = 30, k = 30, target = 500))