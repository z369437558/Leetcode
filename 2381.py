class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        diff=[0 for i in range(len(s))]
        diff[0]=ord(s[0])-ord('a')
        for i in range(1,len(s)):
            diff[i]=ord(s[i])-ord(s[i-1])
        for shift in shifts:
            diff[shift[0]]=diff[shift[0]]-1+shift[2]*2
            if shift[1]+1<len(diff):
                diff[shift[1]+1]=diff[shift[1]+1]+1-shift[2]*2
        diff[0]%=26
        if diff[0]<0:
            diff[0]+=26
        ans=[chr(ord('a')+diff[0])] 
        for i in range(1,len(diff)):
            a = (ord(ans[-1])+diff[i]-ord('a'))%26
            if a<0:
                a+=26
            ans.append(chr(a+ord('a')))
        return ''.join(ans)  
a =Solution()
print(a.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]))