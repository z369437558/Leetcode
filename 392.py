class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p=0
        tot=0
        for i in s:
            for j in range(p,len(t)):
                if i==t[j]:
                    p=j+1
                    tot=tot+1
                    break
        if tot==len(s):
            True
        return False
a = Solution()
a.isSubsequence("abc","ahbgdc")