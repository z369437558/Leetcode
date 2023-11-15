class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        def test(target):
            list1 = nums.copy()
            tot=0
            p=0
            while p<len(list1):
                left=0
                right = len(list1)-1
                while left<right:
                    mid = (left+right)//2+1
                    if list1[mid]-list1[p]>k:
                        right=mid-1
                    else:
                        left=mid
                p=left+1
                tot+=1
            return tot<=target
        nums.sort()
        left=1
        right=len(nums)
        while left<right:
            mid = (left+right)//2
            if test(mid):
                right=mid
            else:
                left=mid+1
        return left
a = Solution()
print(a.partitionArray(nums = [3,6,1,2,5], k = 2))