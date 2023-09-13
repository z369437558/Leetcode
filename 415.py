def main(num1,num2): 
    num1 = list(num1)
    num2 = list(num2)
    num1.reverse()
    num2.reverse()
    if len(num1)<len(num2):
        num1,num2=num2,num1
    for i in range(len(num1)-len(num2)):
        num2.append('0')
    for i in range(len(num2)):
        ans = int(num1[i])+int(num2[i])
        if ans >= 10:
            ans = ans-10
            if i+1<len(num1):
                num1[i+1]=str(int(num1[i+1])+1)
            else:
                num1.append('1')
        num1[i] = str(ans)
    num1.reverse()
    return ''.join(num1)
num1='6994'
num2='36'
print(main(num1,num2))