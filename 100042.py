class Solution:
    def lengthOfLongestSubsequence(self, nums: list[int], target: int) -> int:
        dp = [[-5000 for i in range(target+1)]for j in range(len(nums))]
        for i in range(len(nums)):
            dp[i][nums[i]]=1
        for i in range(1,len(nums)):
            for j in range(target+1):
                if j>=nums[i]:
                    dp[i][j]=max(dp[i-1][j-nums[i]]+1,dp[i-1][j],dp[i][j])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j])
        return max(dp[len(nums)-1][target],-1)
a = Solution()
a.lengthOfLongestSubsequence([4,1,3,2,1,5],7)