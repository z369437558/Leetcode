class Solution:
    def findLHS(self, nums: list[int]) -> int:
        ans=0
        tot={}
        for i in range(len(nums)):
            if nums[i] not in tot:
                tot[nums[i]]=1
            else:
                tot[nums[i]]+=1
        for i in tot.keys():
            if i-1 in tot.keys():
                ans = max(ans,tot[i]+tot[i-1])
        return ans 
a = Solution()
print(a.findLHS([1,3,2,2,5,2,3,7]))