nums = [-1,0,3,5,9,12]
target = 0
left= 0
right = len(nums)-1
while left<right:
    mid = int((left+right)/2)
    if nums[mid]<target:
        left = mid+1
    else:
        right = mid
if nums[right]==target:
    print (right)
else:
    print (-1)