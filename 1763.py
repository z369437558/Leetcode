class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def f(left,right):
            s1 =s[left:right+1]
            set1= set(s1)
            for i in set1:
                if i>='a' and i<='z':
                    if i.upper() not in set1:
                        return False
                if i>='A' and i <='Z':
                    if i.lower() not in set1:
                        return False
            return True
        ans=''
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if f(i,j) and j-i+1>len(ans):
                    ans=s[i:j+1]
        return ans 
a = Solution()
print(a.longestNiceSubstring( "YazaAay"))