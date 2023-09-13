class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        ans=sum(nums[:k])/k
        tot=ans*k
        for i in range(k,len(nums)):
            tot=tot+nums[i]-nums[i-k]
            ans=max(ans,tot/k)
        return ans
a=Solution()
a.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)