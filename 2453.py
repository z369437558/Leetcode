from collections import Counter
class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        dict1 = {}
        nums.sort()
        for i in range(len(nums)):
            if nums[i]%space not in dict1:
                dict1[nums[i]%space]= nums[i]
        for i in range(len(nums)):
            nums[i]=nums[i]%space
        c = Counter(nums)
        max1= 0
        ans = max(nums)
        for k,v in c.items():
            if v>max1:
                ans = dict1[k]
                max1 = v
            else:
                if v==max1:
                    ans = min(dict1[k],ans)
        return ans
a = Solution()
a.destroyTargets(nums = [3,7,8,1,1,5], space = 2)
