class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high+1)]
        dp[0]=1
        for i in range(1,high+1):
            a=0
            b=0
            if i>=zero:
                a = dp[i-zero]
            if i>=one:
                b = dp[i-one]
            dp[i]=a+b
        return sum(dp[low:high+1])

a = Solution()
print(a.countGoodStrings(low = 3, high = 3, zero = 1, one = 1))