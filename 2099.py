class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        index = range(len(nums))
        nums,index = zip(*sorted(zip(nums, index),reverse=True))
        nums = nums[0:k]
        index = index[0:k]
        index,nums = zip(*sorted(zip(index,nums)))
        return nums
a =Solution()
a.maxSubsequence([50,-75],2)