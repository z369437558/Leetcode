class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        a=[1 for i in range(len(nums))]
        b=[1 for i in range(len(nums))]
        ans= [1 for i in range(len(nums))]
        a[0]=nums[0]
        b[-1]=nums[-1]
        for i in range(1,len(nums)):
            a[i]=a[i-1]*nums[i]
        for j in range(len(nums)-2,-1,-1):
            b[j]=b[j+1]*nums[j]
        for i in range(1,len(nums)-1):
            ans[i]=a[i-1]*b[i+1]
        ans[0]=b[1]
        ans[-1]=a[-2]
        return ans
a = Solution()
print(a.productExceptSelf([1,2,3,4]))