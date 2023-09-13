class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        p=0
        ans=[]
        while p<len(intervals):
            s = intervals[p][0]
            e = intervals[p][1]
            for i in range(p+1,len(intervals)):
                start = max(intervals[p][0],intervals[i][0])
                end = min(intervals[p][1],intervals[i][1])
                if end>=start:
                    p=i
                    e = intervals[i][1]
                else:
                    p=i
                    break
            ans.append([s,e])
            if e == intervals[-1][1]:
                break
        return ans
a = Solution()
print(a.merge([[1,3],[2,6],[8,10],[15,18]]))