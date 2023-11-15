class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        totnums=sum(cost)
        ans = 2**53
        def totcost(n):
            t=0
            for i in range(len(nums)):
                t +=abs(n-nums[i])*cost[i]
                if t>=ans:
                    return t
            return t
        z = list(zip(nums,cost))
        z.sort(key = lambda x :x[0])
        if totnums%2==1:
            target = totnums//2+1
            for num in z:
                if  target>num[1]:
                    target-=num[1]
                else:
                    ans = totcost(num[0])
                    break
        if totnums%2==0:
            target = totnums//2
            for i in range(len(z)):
                num = z[i]
                if target>num[1]:
                    target-=num[1]
                else:
                    if target<num[1]:   
                        ans = totcost(num[0])
                    else:
                        ans = totcost((z[i][0]+z[i+1][0])//2)
                    break
        return ans 

a = Solution()
print(a.minCost([735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518],[724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]))