class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        for i in set(ranks):
            if ranks.count(i)>=3:
                return "Three of a Kind"
        for i in set(ranks):
            if ranks.count(i)==2:
                return "Three of a Kind"
        return "High Card"
a = Solution()
a.bestHand(ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"])