from math import ceil
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n-1)]
for i in range(n-1):
    ans = lst[i][0]+lst[i][1]
    for j in range(i+1, n-1):
        k = max(0, ceil((ans-lst[j][1])/lst[j][2]))
        ans = lst[j][1]+k*lst[j][2]+lst[j][0]
    print(ans)
print(0)