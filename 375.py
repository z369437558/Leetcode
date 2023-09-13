class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return self.f(1,n)
    def f(self,a,b):
        if a>b:
            return 0
        elif a==b:
            return 0
        elif a+1==b:
            return a
        else:
            list1 = [max(self.f(a,i-1)+i,self.f(i+1,b)+i) for i in range(a,b+1)]
            return min(list1)
a = Solution()
print(a.getMoneyAmount(3))