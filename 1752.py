class Solution:
    def check(self, nums: list[int]) -> bool:
        nums1 = sorted(nums)
        for i in range(len(nums)):
            if nums1[i:]+nums1[:i]==nums:
                return True
        return False
a=Solution()
a.check([3,4,5,1,2])