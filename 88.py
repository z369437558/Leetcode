nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1 = nums1[0:m]
nums1.extend(nums2)
nums1.sort()
print(nums1)