class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                left=j+1
                right=len(nums)-1
                while left<right:
                    mid = (left+right)//2
                    if nums[i]+nums[j]+nums[mid]<target:
                        left=mid+1
                    else:
                        right=mid
                if left>j+1:
                    if abs(target-nums[i]-nums[j]-nums[left])<abs(target-nums[i]-nums[j]-nums[left-1]):
                        ans.append(nums[i]+nums[j]+nums[left])
                    else:
                        ans.append(nums[i]+nums[j]+nums[left-1])
                else:
                    ans.append(nums[i]+nums[j]+nums[left])
                if left==0:
                    ans.append(nums[i]+nums[j]+nums[left])
        return ans[min(range(len(ans)), key=lambda i: abs(ans[i]-target))]   
a = Solution()
print(a.threeSumClosest([-1,2,1,-4],1))