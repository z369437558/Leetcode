class Solution:
    def minChanges(self, s: str) -> int:
        def fun(i,j):
            if j-i==1:
                if s[i]==s[j]:
                    return 0
                else:
                    return 1
            mid  = (j+i)//2
            return fun(i,mid)+fun(mid+1,j)
        return fun(0,len(s)-1)
a = Solution()
a.minChanges('010010')