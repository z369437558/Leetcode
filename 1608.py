class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(0,1001):
            tot=0
            for j in nums:
                if j>=i:
                    tot+=1
            if tot==i:
                return i
        return -1
a =Solution()
a.specialArray([0,0])