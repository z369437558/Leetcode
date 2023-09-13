class Solution:
    def mergeSimilarItems(self, items1, items2 ) :
        # set1 = set(items1[][0])+set(items2[][0])
        # for i in items1:
        #     if i[0] in set
        items1.sort(key=lambda x:x[0])
        items2.sort(key=lambda x:x[0])
        p1=0
        p2=0
        ans = []
        while p1<len(items1) and p2<len(items2):
            if items1[p1][0]==items2[p2][0]:
                ans.append([items1[p1][0],items1[p1][1]+items2[p2][1]])
                p1=p1+1
                p2=p2+1
            else:
                if items1[p1][0]<items2[p2][0]:
                    ans.append([items1[p1][0],items1[p1][1]])
                    p1=p1+1
                else:
                    if items1[p1][0]>items2[p2][0]:
                        ans.append([items2[p2][0],items2[p2][1]])
                        p2=p2+1
        if p1<len(items1):
            ans.extend(items1[p1:])
        if p2<len(items2):
            ans.extend(items2[p2:])
        return ans
a = Solution()
a.mergeSimilarItems([[26,6],[19,4],[10,1]],[[9,5],[6,9],[18,10],[16,4],[27,4],[17,8]])