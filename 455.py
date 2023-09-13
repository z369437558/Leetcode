class Solution:
    def findContentChildren(self, g,s) -> int:
        g.sort()
        s.sort()
        p=0
        q=0
        ans=0
        while p<len(g) and q<len(s):
            if s[q]>=g[p]:
                ans=ans+1
                p=p+1
                q=q+1
            else:
                p=p+1
        return ans
a= Solution()
a.findContentChildren([10,9,8,7],[5,6,7,8])