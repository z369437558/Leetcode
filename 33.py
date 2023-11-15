class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find(l,r):
            if l>=len(nums):
                return -1
            while l<r:
                mid = (l+r)//2+1
                if nums[mid]<=target:
                    l = mid
                else:
                    r = mid-1 
            if nums[l]==target:
                return l
            else:
                return -1
        left= 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2+1
            if nums[mid]>nums[0]:
                left = mid
            else:
                right = mid-1
        if target<nums[0]:
            return find(left+1,len(nums)-1)
        else:
            return find(0,left)
a = Solution()
print(a.search(nums = [1], target = 0))