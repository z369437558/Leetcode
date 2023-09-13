from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        s=list(s)
        c=Counter(s)
        ans=''
        while c.total()>0:
            for key,value in sorted(c.items(),key=lambda x:x[0]):
                if value>0:
                    ans+=key
                    c[key]-=1
            for key,value in sorted(c.items(),key=lambda x:x[0],reverse=True):
                if value>0:
                    ans+=key
                    c[key]-=1
        return ans

a= Solution()
a.sortString(s="rat")