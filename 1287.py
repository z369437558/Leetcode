import math
arr=[1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]
set1 = set(arr)
p=len(arr)//4
if(len(arr)%4>0):
    p=p+1
for i in set1:
    if arr.count(i)> p:
        print( i)
    if len(arr)<=3:
        if arr.count(i)>=1:
            print( i) 