class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        id_size = [(i,groupSizes[i]) for i in range(len(groupSizes))]
        id_size.sort(key = lambda x:x[1])
        ans=[]
        for i in range(len(id_size)):
            if len(ans)==0 or len(ans[-1])==id_size[i][1] or (i>=1 and id_size[i][1]!=id_size[i-1][1]):
                ans.append([id_size[i][0]])
            else:
                ans[-1].append(id_size[i][0])
        return ans
a = Solution()
a.groupThePeople(groupSizes = [3,3,3,3,3,1,3])