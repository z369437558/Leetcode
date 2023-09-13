ans = 0
grid=[[1,2,4],[3,3,1]]
while len(grid[0])>0:
    list1 = []
    for row in grid:

        max1 = max(row)
        list1.append(max1)
        row.remove(max1)
    ans = ans + max(list1)
print(ans)