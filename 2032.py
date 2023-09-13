class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        set4 = (set1 | set2 |set3)  -(set1 ^ set2 ^ set3)  
        return list(set4)
a = Solution()
a.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3])