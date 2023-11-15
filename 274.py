class Solution:
    def hIndex(self, citations: list[int]) -> int:
        def judge(n):
            t=0
            for i in range(len(citations)):
                if citations[i]>=n:
                    t+=1
            return t>=n
        l=0
        r=len(citations)
        while l<r:
            mid = (l+r)//2+1
            if judge(mid):
                left= mid
            else:
                right=mid-1
        return left
a = Solution()
a.hIndex([3,0,6,1,5])