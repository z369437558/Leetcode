import math
class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def check(n):
            ans=0
            for num in nums:
                ans+=math.ceil(num/n)-1
            return ans<=maxOperations
        left=1
        right = max(nums)
        while left<right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left= mid+1
        return left
a = Solution()
print(a.minimumSize([9],2))