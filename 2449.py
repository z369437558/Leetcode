class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        odd = sorted([num  for num in nums if num %2 ==0])
        even = sorted([num  for num in nums if num %2 ==1])
        oddtarget = sorted([num  for num in target if num %2 ==0])
        eventarget  = sorted([num  for num in target if num %2 ==1])
        plus=0
        minus=0
        for i in range(len(odd)):
            if oddtarget[i]-odd[i]>0:
                plus += (oddtarget[i]-odd[i])//2
            else:
                minus += -(oddtarget[i]-odd[i])//2
        for i in range(len(even)):
            if eventarget[i]-even[i]>0:
                plus += (eventarget[i]-even[i])//2
            else:
                minus += -(eventarget[i]-even[i])//2
        return plus
a = Solution()
print(a.makeSimilar(nums = [8,12,6], target = [2,14,10]))