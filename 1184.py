distance=[7,10,1,12,11,14,5,0]
start=7
destination=2 
if start>destination:
    start,destination=destination,start
if start==destination:
    print (0)
print (sum(distance[start:destination]),sum(distance))