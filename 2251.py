class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        ans =[0 for i  in range(len(people))]
        diff={}
        for flower in flowers:
            if flower[0] in diff:
                diff[flower[0]]+=1
            else:
                diff[flower[0]]=1
            if (flower[1]+1) in diff:
                diff[flower[1]+1]-=1
            else:
                diff[flower[1]+1]=-1
        diff = sorted(diff.items(),key = lambda x:(x[0],x[1]))
        q= sorted([(people[i],i) for i in range(len(people))])
        list1 = diff
        flowerposition = 0
        tot=0
        for p,i in q:
            while flowerposition<len(list1) and list1[flowerposition][0] <=p:
                tot+=list1[flowerposition][1]
                flowerposition+=1
            ans[i]+=tot
        return ans
a = Solution()
print(a.fullBloomFlowers(flowers = [[19,37],[19,38],[19,35]], people = [6,7,21,1,13,37,5,37,46,43]))