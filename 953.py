class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        return words==sorted(words,key=lambda w:[order.index(x) for x in w])
a=Solution()
a.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")