def main(arr):
    arr1=arr[:]
    arr.sort()
    ans=[1]
    ans1=[]
    dict1={arr[0]:1}
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            ans.append(ans[i-1])
        else:
            ans.append(ans[i-1]+1)
        dict1[arr[i]]=ans[i]
    for i in range(len(arr1)):
        ans1.append(dict1[arr1[i]])
    return ans1
arr=[40,10,20,30]
print(main(arr))