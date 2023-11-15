class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def dp(l,r):
            if nums[l:r]==sorted(nums[l:r],reverse=True):
                nums[l:r]= sorted(nums[l:r])
                return False
            if dp(l+1,r)==False:
                for i in range(l+1,r):
                    if nums[i]>nums[l]:
                        nums[l],nums[i]=nums[i],nums[l]
                        return True
        dp(0,len(nums))
        return nums
a = Solution()
print(a.nextPermutation([2,3,1]))