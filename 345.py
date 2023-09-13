class Solution:
    def reverseVowels(self, s: str) -> str:
        s1 = list(s)
        list1 = ['a','e','i','o','u','A','E','I','O','U']
        left=0
        right=len(s)-1
        while left<right:
            while left<len(s) and s[left] not in list1:
                left+=1
            while right>=0 and s[right] not in list1:
                right-=1
            if left>=right:
                break
            s1[left],s1[right]=s1[right],s1[left]
            left+=1
            right-=1
        return ''.join(s1)
a=Solution()
a.reverseVowels('hello')