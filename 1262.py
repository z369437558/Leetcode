class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        n= len(nums)
        dp=[[-4*10**8 for i in range(3)] for i in range(n)]
        dp[0][0]=0
        dp[0][nums[0]%3]=nums[0]

        for i in range(1,n):
            for j in range(3):
                dp[i][j]=max(dp[i-1][j],dp[i-1][(j-nums[i]%3+3)%3]+nums[i])
        return max(dp[n-1][0],0)
a = Solution()
print(a.maxSumDivThree(nums = [2,19,6,16,5,10,7,4,11,6]))