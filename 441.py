class Solution:
    def arrangeCoins(self, n: int) -> int:
        left=1
        right=int((n*2)**0.5)
        while left<right:
            mid = (left+right)//2+1
            if mid*mid+mid<=n*2:
                left=mid
            else:
                right=mid-1
        return left
a= Solution()
a.arrangeCoins(3)