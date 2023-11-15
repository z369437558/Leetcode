from collections import Counter 
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n ==0:
            return len(tasks)
        c = Counter(tasks)
        list1 = c.most_common()
        m = list1[0][1]
        tot=0
        for i in range(len(list1)):
            if list1[i][1]==m:
                tot+=1
        if len(tasks)-tot*m<=(n-tot+1)*(m-1):
            return (m-1)*n+m+tot-1
        else:
            return len(tasks)
a = Solution()
print(a.leastInterval(tasks = ["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], n = 7))