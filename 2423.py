from collections import Counter 
class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        if c.most_common(2)[0][1]-c.most_common(2)[1][1]==1:
            return True
        else:
            return False
a=Solution()
a.equalFrequency("bac")