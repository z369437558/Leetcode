class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        def fun(left,right):
            t= 1
            for i in range(left,right+1):
                t*=powers[i]
                t=t%(10**9+7)
            return t
        s = bin(n)[2:]
        s=s[-1::-1]
        powers=[]
        for i in range(len(s)):
            if s[i]=='1':
                powers.append(2**i)
        ans=[]
        for q in queries:
            ans.append(fun(q[0],q[1]))
        return ans
a = Solution()
a.productQueries(2,[[0,0]])