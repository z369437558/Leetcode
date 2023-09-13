class Solution:
    def insert(self, intervals, newInterval) :
        p=0
        q=0
        flag1=True
        flag2=True
    
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[0]>interval[1]:
                p=i+1
                flag1=True
            elif newInterval[0] in range(interval[0],interval[1]+1):
                p=i
                flag1=False
            else:
                break
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[1]>interval[1]:
                q=i+1
                flag2=True
            elif newInterval[1] in range(interval[0],interval[1]+1):
                q=i
                flag2=False
            else:
                break
        if flag1==True and flag2==True:
            if p!=q:
                intervals[p][0]=newInterval[0]
                intervals[p][1]=newInterval[1]
                del intervals[p+1:q]
            else:
                intervals.insert(p,newInterval)
        if flag1==False and flag2==False:
            intervals[p][1]=intervals[q][1]
            del intervals[p+1:q+1]
        if flag1==True and flag2==False:  
            intervals[p][0]=newInterval[0]
            intervals[p][1]=intervals[q][1]
            del intervals[p+1:q+1]
        if flag1==False and flag2==True:
            intervals[p][1]=newInterval[1]
            del intervals[p+1:q]        
        return intervals
a = Solution()
print(a.insert([[2,7],[8,8],[10,10],[12,13],[16,19]], [9,17]))