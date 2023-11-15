class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        ans=[]
        def gcd(x,y):
            if y==0:
                return x
            x,y=max(x,y),min(x,y)
            return gcd(y,x%y)
        for i in range(2,n+1):
            for j in range(1,i):
                if gcd(i,j)==1:
                    ans.append(str(j)+'/'+str(i))
        return ans
a = Solution()
a.simplifiedFractions(3)