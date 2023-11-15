class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        def find(list1,target):
            left = 0
            right =len(list1)-1
            while left<right:
                mid = (left+right)//2
                if list1[mid]>=target:
                    right=mid
                else:
                    left=mid+1
            return list1[left]
        ans = [-10**5,10**5]
        for left in range(-10**5,10**5+1):
            right = left
            for j in range(len(nums)):
                if nums[j][-1]<left:
                    return ans
                right = max(right,find(nums[j],left))
            if right-left<ans[1]-ans[0]:
                ans = [left,right]
            if right-left==ans[1]-ans[0] and left<ans[0]:
                ans = [left,right]
        return ans

a = Solution()
print(a.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))