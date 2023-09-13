class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        now=0
        ans=[]
        for i in range(len(nums)):
            ans.append((now*2+nums[i])%5==0)
            now = (now*2+nums[i])%10
        return ans
a= Solution()
a.prefixesDivBy5([0,1,1,1,1,1])