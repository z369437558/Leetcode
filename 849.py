class Solution:
    def maxDistToClosest(self, seats) -> int:
        # left=0
        # right=len(seats)
        # mid=0
        # while left<right:
        #     mid = (left+right)//2+1
        #     if self.find(mid,seats):
        #         left = mid
        #     else:
        #         right=mid-1
        # return left
        tot=0
        max1=0
        ans=[]
        for i in range(len(seats)):
            if seats[i]==0:
                tot=tot+1
            else:
                if tot>0:
                    max1= tot
                    ans.append(max1)
                    tot=0
        if tot>0:
            max1= tot
            ans.append(max1)
            tot=0
        for i in range(len(ans)):
            ans[i]=(ans[i]-1)//2
        left=0
        right=0
        for i in seats:
            if i==0:
                left=left+1
            else:
                break
        for i in range(len(seats)-1,-1,-1):
            if seats[i]==0:
                right=right+1
            else:
                break
        return max(max(ans)+1,left,right)
    # def find(self,x,seats):
    #     for i in range(len(seats)):
    #         left = max(0,i-x+1)
    #         right = min(len(seats)-1,i+x-1)
    #         if sum(seats[left:right+1])==0:
    #             return True
    #     return False

a = Solution()
print(a.maxDistToClosest(seats =[1,0,0,0]))