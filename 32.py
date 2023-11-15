class Solution:
    def longestValidParentheses(self, s: str) -> int:
        list1 = []
        t=0
        tt=0
        for i in range(len(s)):
            if s[i]=='(':
                list1.append(tt)
                tt=0
                t+=1
            if s[i]==')':
                if t>0:
                    t-=1
                    tt+=1
        list1.append(tt)
        tot=0
        ans=0
        for i in range(len(list1)):
            if list1[i]>0:
                tot+=list1[i]
                ans=max(tot,ans)
            else:
                tot=0
        return ans*2
a = Solution()
a.longestValidParentheses(s = "()(())")