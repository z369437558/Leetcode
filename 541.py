class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=''
        while len(s)>=2*k:
            ans+=''.join(reversed(s[:k]))
            ans+=s[k:k*2]
            s=s[2*k:]
        if len(s)<k:
            ans+=''.join(reversed(s))
        else:
            ans+=''.join(reversed(s[:k]))
            ans+=s[k:]
        return ans
a= Solution()
a.reverseStr(s = "abcdefg", k = 2)