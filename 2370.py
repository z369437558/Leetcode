class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[[0 for _ in range(26)]for _ in range(len(s))]
        dp[0][ord(s[0])-ord('a')]=1
        for i in range(1,len(s)):
            for j in range(26):
                dp[i][j]=dp[i-1][j]
            for x in range(k+1):
                if ord(s[i])-ord('a')-x>=0:
                    dp[i][ord(s[i])-ord('a')]=max(dp[i][ord(s[i])-ord('a')],dp[i-1][ord(s[i])-ord('a')-x]+1)
                if ord(s[i])-ord('a')+x<26:
                    dp[i][ord(s[i])-ord('a')]=max(dp[i][ord(s[i])-ord('a')],dp[i-1][ord(s[i])-ord('a')+x]+1)
        return max(dp[-1])

a = Solution()
print(a.longestIdealString(s = "acfgbd", k = 2))