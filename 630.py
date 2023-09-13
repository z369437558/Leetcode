class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        # courses.sort(key=lambda x:x[1])
        for i in range(len(courses)):
            for j in range(i+1,len(courses)):
                if courses[i][0]>=courses[j][0] and courses[i][1]>=courses[j][1]:
                    courses[i],courses[j] = courses[j],courses[i]
        ans=0
        tot=0
        for i in range(len(courses)):
            if tot+courses[i][0]<=courses[i][1]:
                tot+=courses[i][0]
                ans+=1
        return ans
a=Solution()
a.scheduleCourse([[5,5],[4,6],[2,6]])