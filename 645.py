from collections import Counter 
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        set_right=set(range(1,len(nums)+1))
        set_error=set(nums)
        c=Counter(nums)
        return [int(c.most_common(1)[0][0]),list(set_right-set_error)[0]]
a =Solution()
a.findErrorNums([1,1])