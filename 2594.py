class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        # @cache
        # def f(n,m):
        #     if n==0:
        #         return 0
        #     if m==0:
        #         return ranks[0]*n*n
        #     return min(list(map(lambda i:max(f(n-i,m-1),ranks[m]*i*i),range(n+1))))
        # return f(cars,len(ranks)-1)
        m1=len(ranks)
        n1=cars
        f=[[0 for i in range(m1)] for j in range(n1+1)]
        # for i in range(n1+1):
        #     f[i][0]=ranks[0]*i*i
        for n in range(1,n1+1):
            for m in range(len(ranks)):
                if m==0:
                    f[n][m]=ranks[0]*n*n
                else:
                    f[n][m]=min(list(map(lambda i:max(f[n-i][m-1],ranks[m]*i*i),range(n+1))))
        return f[cars][len(ranks)-1]
a= Solution()
print(a.repairCars([4,2,3,1],10))