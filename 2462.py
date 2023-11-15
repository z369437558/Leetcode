from sortedcontainers import SortedList
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        ans=0
        p1 = candidates-1
        p2 = -candidates
        if n>2*candidates:
            leftlist = SortedList(costs[:p1+1])
            rightlist  = SortedList(costs[p2:])  
        sortedlist =SortedList(costs) 
        while k>0:
            if n>2*candidates:
                if leftlist[0]<=rightlist[0]:
                    ans+=leftlist[0]
                    sortedlist.remove(leftlist[0])
                    leftlist.pop(0)
                    p1+=1
                    leftlist.add(costs[p1])
                else:
                    ans+=rightlist[0]
                    sortedlist.remove(rightlist[0])
                    rightlist.pop(0)
                    p2-=1
                    rightlist.add(costs[p2])
            else:
                ans+=sortedlist[0]
                sortedlist.pop(0)
            k-=1
            n-=1
        return ans

         
a = Solution()
a.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)