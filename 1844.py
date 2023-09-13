class Solution:
    def replaceDigits(self, s: str) -> str:
        ans=''
        for i in range(0,len(s)-len(s)%2,2):
            ans+=s[i]
            ans+=chr(ord(s[i])+int(s[i+1]))
        if len(s)%2==1:
            ans+=s[-1]
        return ans
a=Solution()
a.replaceDigits('a1b2c3d4e')