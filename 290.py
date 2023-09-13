class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        set1 = set()
        dict1={}
        if len(list(pattern))!=len(s.split(' ')):
            return False
        s = s.split(' ')
        if len(set(list(pattern)))!=len(set(s)):
            return False
        
        for i,word in enumerate(pattern):
            if word not in set1:
                dict1[word]=s[i]
                set1.add(word)
        for i,word in enumerate(pattern):
            if s[i]!=dict1[word]:
                return False
        return True
a = Solution()
a.wordPattern("abba","dog cat cat fish")