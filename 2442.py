class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        def reverse(num):
            return int(str(num)[-1::-1])
        n = len(nums)
        for i in range(n):
            nums.append(reverse(nums[i]))
        return len(set(nums))
a = Solution()
a.countDistinctIntegers([1,13,10,12,31])