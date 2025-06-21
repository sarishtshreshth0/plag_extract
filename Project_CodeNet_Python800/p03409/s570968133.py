n = int(input())
ab = []
for i in range(n):
    ab.append(list(map(int,input().split())))
cd = []
for i in range(n):
    cd.append(list(map(int,input().split())))
cd.sort(key=lambda x:x[0])
ab.sort(key=lambda x:x[1],reverse=True)
ab.sort(key=lambda x:x[0])
tmp = -1
ans = 0
for i in range(n):
    ma = -1
    for j in range(n):
        if cd[i][0] > ab[j][0]:
            if ab[j][1] > ma and cd[i][1] > ab[j][1]:
                ma = ab[j][1]
                tmp = j
    if tmp != -1:
        ans+=1
        ab[tmp][1] = 201
    tmp = -1
    ma = -1
print(ans)