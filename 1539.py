class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        # p=arr[-1]-len(arr)
        # if k>p:
        #     return arr[-1]+k-p
        left=0
        right=len(arr)-1
        while left<right:
            mid=(left+right)//2+1
            if arr[mid]-mid-1>=k:
                right=mid-1
            else:
                left=mid
        p=arr[left]-left-1
        return arr[left]+k-p
a = Solution()
print(a.findKthPositive([1,2],1))