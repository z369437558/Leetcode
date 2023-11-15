class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        for i in range(len(distance)):
            if chr(ord('a')+i) not in s:
                distance[i]=0
        distance1=[0 for i in range(26)]
        dict1={}
        for i,char in enumerate(s):
            if char in dict1:
                distance1[ord(char)-ord('a')]=i-dict1[char]-1
            else:
                dict1[char]=i
        return distance1==distance
a = Solution()
a.checkDistances(s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])