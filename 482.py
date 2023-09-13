class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace('-','').upper()
        mod= len(s)%k
        ans=s[0:mod]
        for i in range(0,len(s),k):
            if ans!='':
                ans=ans+'-'+s[i:i+k]
            else:
                ans='-'+s[i:i+k]
        return ans

a=Solution()
a.licenseKeyFormatting("5F3Z-2e-9-w",4)