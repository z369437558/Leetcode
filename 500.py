class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        ans=[]
        row1=set(list("qwertyuiop"))
        row2=set(list("asdfghjkl"))
        row3=set(list("zxcvbnm"))
        def f(word):
            word=word.lower()
            if set(list(word))&row1==set(list(word)):
                return True
            if set(list(word))&row2==set(list(word)):
                return True
            if set(list(word))&row3==set(list(word)):
                return True
            return False
        for word in words:
            if f(word):
                ans.append(word)
        return ans
a=Solution()
a.findWords(words = ["Hello","Alaska","Dad","Peace"])