class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        dp=[[-999999,-999999] for i in range(len(prices))]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for day in range(1,len(prices)):
            dp[day][0]= max(dp[day-1][1]+prices[day]-fee,dp[day-1][0])
            dp[day][1] = max(dp[day-1][0]-prices[day],dp[day-1][1])
        return dp[-1][0]
a = Solution()
a.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2)