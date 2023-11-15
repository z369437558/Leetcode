class Solution:
    def longestPalindrome(self, s: str) -> str:
        def judge(s):
            s1 = s[len(s)//2+len(s)%2:]
            return s[:len(s)//2]==s1[::-1]
        if len(s)<=1:
            return s
        max1=0
        ans=s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j] and j-i+1>max1:
                    if judge(s[i:j+1]):
                        max1 = j-i+1
                        ans = s[i:j+1]
        return ans 
a  = Solution()
print(a.longestPalindrome("abcba"))
