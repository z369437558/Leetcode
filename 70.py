n=3
f=[0 for i in range(50)]
f[1]=1
f[2]=2

if n>=3:
    for i in range(3,n+1):

        f[i]=f[i-1]+f[i-2]