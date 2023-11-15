class Solution:
    def hIndex(self, citations: list[int]) -> int:
        def check(target):
            left = 0
            right = len(citations)-1
            while left<right:
                mid = (left+right)//2+1
                if citations[mid]<target:
                    left=mid
                else:
                    right=mid-1
            if citations[left]>=target:
                return len(citations)-left>=target
            else:
                return len(citations)-left-1>=target
        left=0
        right=1000
        while left<right:
            mid = (left+right)//2+1
            if check(mid):
                left= mid
            else:
                right=mid-1
        return left
a = Solution()
print(a.hIndex(citations = [1,2,2]))