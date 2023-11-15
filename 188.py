class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        dp=[[[-9999999,-9999999] for j in range(102)] for i in range(len(prices))]
        # dp[天数][完成交易数][是否持有股票]
        dp[0][0][0]=0
        dp[0][0][1]=-prices[0]
        for day in range(1,len(prices)):
            for trade in range(0,k+1):
                dp[day][trade][0]= max(dp[day-1][trade-1][1]+prices[day],dp[day-1][trade][0])
                dp[day][trade][1]= max(dp[day-1][trade][0]-prices[day],dp[day-1][trade][1])
        ans=0
        for i in range(k+1):
           ans = max(ans,dp[-1][i][0])
        return ans
a = Solution()
print(a.maxProfit(k = 2, prices=[3,2,6,5,0,3]))