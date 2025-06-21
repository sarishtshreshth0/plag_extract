n = int(input())
data = []
for i in range(n-1):
    c,s,f = map(int,input().split())
    s //= f
    data.append((c,s,f))
for i in range(n):
    if i == n-1:
        print(0)
        break
    for j in range(i,n-1):
        if j == i:
            ans = data[j][0]+data[j][1]*data[j][2]
            continue
        ans = (max((ans-1)//data[j][2]+1,data[j][1])*data[j][2]) + data[j][0]
    print(ans)