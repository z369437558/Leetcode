class Solution:
    def canJump(self, nums: list[int]) -> bool:
        p=0
        for i in range(len(nums)):
            if i>p:
                return False
            p = max(p,nums[i]+i)
        return True
a = Solution()
a.canJump([2,3,1,1,4])