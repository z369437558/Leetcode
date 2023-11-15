class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        dp= [[-9999999 for i in range(len(satisfaction)+1)] for j in range(len(satisfaction))]
        for i in range(len(satisfaction)):
            dp[i][0]=0
        for n in range(len(satisfaction)):
            for m in range(n+2):
                dp[n][m] = max(dp[n-1][m-1]+m*satisfaction[n],dp[n-1][m])
        return max(dp[-1])
a  = Solution()
print(a.maxSatisfaction(satisfaction = [-1,-8,0,5,-9]))