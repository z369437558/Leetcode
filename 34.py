class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if nums==[]:
            return [-1,-1]
        left=0
        right=len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>=target:
                right=mid
            else:
                left=mid+1
        ans1=left
        left=0
        right=len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>target:
                right=mid
            else:
                left=mid+1       
        ans2 = left
        if nums[ans2]!=target:
            ans2-=1
        if nums[ans1]!=target and nums[ans2]!=target:
            return [-1,-1]
        return (min(ans1,ans2),max(ans1,ans2))
a = Solution()
print(a.searchRange(nums = [5,7,7,8,8,10], target = 6))