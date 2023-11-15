class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #dp[天数][当天结束是什么状态 0：不持不冷冻 1：不持有冷冻 2：持有]
        dp=[[-99999999,-99999999,-9999999] for i in range(len(prices))]
        dp[0][0]=0
        dp[0][2]=-prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = dp[i-1][2]+prices[i]
            if i>=2:
                dp[i][2] = max(dp[i-1][0]-prices[i],dp[i-2][1]-prices[i])
            else:
                dp[i][2] = max(dp[i-1][0]-prices[i],dp[i-1][2])
        return max(dp[-1][0],dp[-1][1])
a = Solution()
print(a.maxProfit([1,2,4]))