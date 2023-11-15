class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        ans=[]
        presum=[nums[0]]
        for i in range(1,len(nums)):
            presum.append(presum[i-1]+nums[i])
        for i in range(len(queries)):
            left=0
            right=len(nums)-1
            while left<right:
                mid =(left+right)//2+1
                if presum[mid]<=queries[i]:
                    left=mid
                else:
                    right=mid-1
            if presum[left]<=queries[i]:
                ans.append(left+1)
            else:
                ans.append(0)
        return ans
a= Solution()
print(a.answerQueries(nums = [4,5,2,3], queries = [1]))