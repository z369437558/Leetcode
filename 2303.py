class Solution:
    def calculateTax(self, brackets, income: int) -> float:
        ans=0
        for i,bracket in enumerate(brackets):
            if i==0:
                down=0
            else:
                down = brackets[i-1][0]
            if income> bracket[0]:
                ans= ans +(brackets[i][0]-down)*bracket[1]/100
            else:
                ans = ans+ (income - brackets[i-1][0])*bracket[1]/100
        return ans
a= Solution()
a.calculateTax([[1,0],[4,25],[5,50]],2)