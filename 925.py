class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1=0
        p2=0
        while p1<len(name) and p2<len(typed):
            if name[p1]!=typed[p2]:
                return False
            while ((p1+1 < len(name) and name[p1]!=name[p1+1]) or p1==len(name)-1) and p2+1<len(typed) and typed[p2]==typed[p2+1]:
                    p2+=1
            p1+=1
            p2+=1
        if (p1<len(name) and p2>=len(typed)) or (p1>=len(name) and p2<len(typed)):
            return False
        return True
a=Solution()
a.isLongPressedName(name = "vtkgn", typed = "vttkgnn")