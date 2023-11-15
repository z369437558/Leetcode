class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        def fun(list1):
            c = Counter(list1)
            return len(c)
        ans=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                ans+=fun(nums[i:j+1])**2
        return ans%(10**9+7)
a = Solution()
a.sumCounts([1,2,1])