class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        p1=0
        p2=0
        q1=0
        q2=0
        list1 = []
        presum1=[]
        presum2=[]
        t=0
        for i in range(len(nums1)):
            t+=nums1[i]
            presum1.append(t)
        t=0
        for i in range(len(nums2)):
            t+=nums2[i]
            presum2.append(t)
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]!=nums2[p2]:
                if nums1[p1]<nums2[p2]:
                    p1+=1
                else:
                    p2+=1
            else:
                list1.append((p1,p2))
        for i in range(len(list1)-1):
            p1,p2=list1[i]
            q1,q2=list1[i+1]
            ans+=max(presum1[q1]-presum1[p1],presum2[q2]-presum2[p2])
        return ans
a = Solution()
a.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9])