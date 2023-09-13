class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(' ')
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i][-1]> s[j][-1]:
                    s[i],s[j]=s[j],s[i]
        for i in range(len(s)):
            s[i]=s[i][:-1]
        return ' '.join(list(s))
        
a=Solution()
a.sortSentence("is2 sentence4 This1 a3")