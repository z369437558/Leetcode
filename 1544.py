class Solution:
    def makeGood(self, s: str) -> str:
        s= list(s)
        while True:
            flag=0
            i=0
            while i+1<len(s):
                if abs(ord(s[i])-ord(s[i+1]))==abs(ord('a')-ord('A')):
                    del s[i:i+2]
                    flag=1
                else:
                    i+=1
            if flag==0:
                break
        return ''.join(s)
a=Solution()
a.makeGood('abBAcC')