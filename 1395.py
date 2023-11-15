class Solution:
    def numTeams(self, rating: list[int]) -> int:
        def  find1(index,prerate,n):
            if n==1:
                self.ans+=bigger[index-1]
                return 
            for i in range(index,len(rating)):
                if rating[i]>prerate:
                    find1(i+1,rating[i],n-1)

        def  find2(index,prerate,n):
            if n==1:
                self.ans+=smaller[index-1]
                return 
            for i in range(index,len(rating)):
                if rating[i]<prerate:
                    find2(i+1,rating[i],n-1)
        bigger=[0 for i in range(len(rating))]
        smaller=[0 for i in range(len(rating))]
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[j]>rating[i]:
                    bigger[i]+=1
                if rating[j]<rating[i]:
                    smaller[i]+=1
        self.ans = 0
        find1(0,0,3)
        find2(0,100005,3)
        return self.ans

a = Solution()
print(a.numTeams([2,5,3,4,1]))