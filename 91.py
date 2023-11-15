class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        ans=[[s[0]]]
        for i in range(1,len(s)):
            for j in range(len(ans)):
                if int(ans[j][-1]+s[i])>=1 and int(ans[j][-1]+s[i])<=26:
                    ans.append(ans[j][:-1]+[ans[j][-1]+s[i]])
                if s[i]!='0':
                    ans[j].append(s[i])

        return len(ans)
a = Solution()
print(a.numDecodings("111111111111111111111111111111111111111111111"))