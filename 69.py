def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    left = 0
    right = x
    while left<right:
        mid = int((left+right)/2)
        if mid*mid<x and (mid+1)*(mid+1)<=x:
            left=mid+1
        else:
            right = mid
    return right
print(mySqrt(4))
