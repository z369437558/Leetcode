class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def dfs(s):
            if s=='':
                return True
            flag = False
            for word in wordDict:
                if s.startswith(word):
                    flag = flag or dfs(s[len(word):])
            return flag
        set1 = set(list(s))
        set2 = set(list(''.join(wordDict)))
        if set2<set1:
            return False
        return dfs(s)
a = Solution()
a.wordBreak(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", wordDict =["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])