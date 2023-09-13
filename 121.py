prices=[7,1,5,3,6,4] 
max1=[0 for i in range(len(prices))]
max1[-1]= prices[-1]
ans = 0
for i in range(len(prices)-2,-1,-1):
    if prices[i]>max1[i+1]:
        max1[i]=prices[i]
    else:
        max1[i]=max1[i+1]
for i in range(1,len(prices)):
    if ans< max1[i]-prices[i-1]:
        ans = max1[i]-prices[i-1]