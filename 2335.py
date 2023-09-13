class Solution:
    def fillCups(self, amount) -> int:
        ans=0
        amount.sort()
        while min(amount)!=0:
            amount[2]=amount[2]-1
            amount[1]=amount[1]-1
            ans=ans+1
            amount.sort()
        ans= ans + max(amount)
        return ans
            

a=Solution(
)
a.fillCups([5,4,4])