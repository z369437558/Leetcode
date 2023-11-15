import queue
class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        b=[0 for i in range(len(arr))]
        q = queue.Queue()
        q.put(start)
        while q.qsize():
            now=q.get()
            b[now]=1
            if arr[now]==0:
                return True
            if now+arr[now] in range(len(arr)) and b[now+arr[now]]==0:
                q.put(now+arr[now])
            if now-arr[now] in range(len(arr)) and b[now-arr[now]]==0:
                q.put(now-arr[now])
        return False
a = Solution()
print(a.canReach(arr = [3,0,2,1,2], start = 2))