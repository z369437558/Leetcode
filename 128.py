class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]]=1
        if nums == []:
            return 0
        ans=1
        nums = list(set(nums))
        for i in range(len(nums)):
            now =nums[i]+1
            while now in dict1:
                dict1[nums[i]]+=dict1[now]
                ans=max(ans,dict1[nums[i]])
                if dict1[now]>1:
                    break
                now = now+1
        return ans 
a = Solution()
print(a.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))