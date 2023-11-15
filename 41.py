class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]]=1
        for i in range(1,max(max(nums)+2,2)):
            if i not in dict1:
                return i 
a = Solution()
print(a.firstMissingPositive(nums = [3,4,-1,1]))