import math
ans=1
tot=0
left = 44
right = 9556
for i in range(left,right+1):
    ans*=i
while ans%10==0:
    tot+=1
    ans=ans//10
digits= int(math.log10(ans))+1
ans1 = ans //(10**(digits-5))
ans2 = ans % 100000
if digits>10:
    s=str(ans1)+'...'+str(ans2)
else:
    s = str(ans)
s+='e'+str(tot)
print(s)