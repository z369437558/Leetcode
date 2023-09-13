import math
class Solution:


    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        tot=0
        for i in range(1,n+1):
            if isPrime(i):
                tot+=1
        return math.factorial(tot)*math.factorial(n-tot)%1000000007
a= Solution()
a.numPrimeArrangements(5)