class Solution:
    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
        for i in range(len(nums)):
            if s[i]=='R':
                nums[i]+=d
            if s[i]=='L':
                nums[i]-=d
        nums.sort()
        ans=0
        dis=[]
        for i in range(len(nums)-1):
            dis.append(nums[i+1]-nums[i])
        t=len(dis)
        p=0
        while p<len(dis):
            ans+=t*(p+1)*dis[p]
            t-=1
            p+=1
            ans%=(10**9+7)
        return ans
a = Solution()
a.sumDistance(nums = [-10,-13,10,14,11], s = "LRLLR", d = 2)