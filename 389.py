from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        return sorted((c2-c1).elements())[0]
a =Solution()
print(a.findTheDifference("abcd","abcde"))