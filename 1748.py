from collections import Counter
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        c= Counter(nums)
        ans=0
        for i,val in c.items():
            if val==1:
                ans+=i
        return ans
a= Solution()
a.sumOfUnique([1,2,3,4,5])