class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        def f(m):
            for i in range(len(nums)-m+1):
                if i==0:
                    if sum1[i+m-1]>=target:
                        return True
                else:
                    if sum1[i+m-1]-sum1[i-1]>=target:
                        return True
            return False
        if sum(nums)<target:
            return 0
        t=0
        sum1=[]
        for i in range(len(nums)):
            t+=nums[i]
            sum1.append(t)
        left=1
        right=len(nums)
        while left<right:
            mid = (left+right)//2
            if f(mid):
                right=mid
            else:
                left=mid+1
        return left
a =Solution()
print(a.minSubArrayLen(5,[2,3,1,1,1,1,1]))