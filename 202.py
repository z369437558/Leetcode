class Solution:
    def isHappy(self, n: int) -> bool:
        set1 =set()
        set1.add(n)
        while True:
            s = str(n)
            ss= list(s)
            n = sum(int(i)**2 for i in ss)
            if n in set1:
                return False
            if n==1:
                return True
a = Solution()
a.isHappy(7)