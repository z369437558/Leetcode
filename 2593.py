class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums=sorted(nums)
        if len(nums)==1:
            return 0
        p=0
        q=1
        ans=0
        while q<len(nums):
            if nums[q]>nums[p]:
                ans+=1
                p+=1
            q+=1
        return ans
a = Solution()
a.maximizeGreatness(nums = [1,3,5,2,1,3,1])