class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        forbidden.sort()
        list0=[0]
        list1=[]
        t=[]
        set1=set()
        ans=0
        while len(list0) or len(list1):
            if x in list0 or x in list1:
                return ans
            t=[]
            t1=[]
            while len(list0):
                if list0[-1]+a<=5000 and list0[-1]+a not in forbidden and list0[-1]+a not in set1:
                    t.append(list0[-1]+a)
                    set1.add(list0[-1]+a)
                if list0[-1]-b>=0 and list0[-1]-b not in forbidden and list0[-1]-b not in set1:
                    t1.append(list0[-1]-b)
                    set1.add(list0[-1]-b) 
                list0.pop()

            while len(list1):
                if list1[-1]+a<=5000 and list1[-1]+a not in forbidden and list1[-1]+a not in set1:
                    t.append(list1[-1]+a)
                    set1.add(list1[-1]+a)
                list1.pop()
            list0=t
            list1=t1
            ans+=1
        return -1
        
a= Solution()
print(a.minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11))