class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            list1 = nums[i:i+k+1]
            set1 = set(list1)
            if len(list1)!=len(set1):
                return True
        return False
a = Solution()
print(a.containsNearbyDuplicate([1,1],2))