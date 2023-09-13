class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        t=0
        s1=''
        ans=''
        for i in range(len(s)):
            s1+=s[i]
            if s[i]=='(':
                t+=1
            else:
                t-=1
            if t==0:
                ans+=s1[1:-1]
        return ans
a = Solution()
a.removeOuterParentheses("(()())(())")