class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        set1=set()
        def f(left,target):
            right=len(nums)-1
            while left<right:
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid
            if nums[right]==target:
                return True
            return False
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if f(j+1,-nums[i]-nums[j]):
                    set1.add((nums[i],nums[j],-nums[i]-nums[j]))
        return list(set1)
                    
a= Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))