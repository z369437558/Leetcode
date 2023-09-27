class Solution:
    def secondHighest(self, s: str) -> int:
        set1 = set()
        for i in s:
            if i in "0123456789":
                set1.add(int(i))
        a = sorted(list(set1))
        if len(a)<2:
            return -1
        return a[1]
a = Solution()
a.secondHighest("ck077")