class Solution:
    def jump(self, nums: list[int]) -> int:
        dp=[10000 for i in range(len(nums))]
        dp[0]=0
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i+j<len(nums):
                    dp[i+j]=min(dp[i+j],dp[i]+1)
        return dp[-1]
a = Solution()
a.jump(nums = [2,3,1,1,4])