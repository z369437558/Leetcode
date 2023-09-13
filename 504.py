class Solution:
    def convertToBase7(self, num: int) -> str:
        ans=''
        flag=0
        if num<0:
            flag=1
            num=-num
        while num>=7:
            ans+=str(num%7)
            num=num//7
        ans+=str(num)
        if flag==1:
            ans+='-'
        return ''.join(reversed(ans))
a = Solution()
a.convertToBase7(100)