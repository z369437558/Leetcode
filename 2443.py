class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def reverse(n):
            return int(str(n)[-1::-1])
        ans=[False for i in range(num*10+10)]
        for i in range(num+10):
            ans[i+reverse(i)]=True
        return ans[num]
a =Solution()
a.sumOfNumberAndReverse(0)