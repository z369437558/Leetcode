class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p=1
        while p<len(nums)-1:
            while nums[p-1]==nums[p] and nums[p]==nums[p+1]:
                del nums[p+1]
            p+=1
        return len(nums)
a =Solution()
a.removeDuplicates([1,1,1])