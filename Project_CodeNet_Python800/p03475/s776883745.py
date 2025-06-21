n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]

if n ==1:
    print(0)
    exit()

res = [0]
res.append(ab[n-2][0]+ab[n-2][1])

for i in range(n-3,-1,-1):
    temp = ab[i][0]+ab[i][1]
    if temp <= ab[i+1][1]:
        res.append(res[-1])
    else:
        for j in range(i,n-2):
            if temp <= ab[j+1][1]:
                temp = ab[j+1][1] + ab[j+1][0]
            else:
                if temp % ab[j+1][2] ==0:
                    temp += ab[j+1][0]
                else:
                    temp = ((temp//ab[j+1][2])+1) * ab[j+1][2] +ab[j+1][0]
        res.append(temp)

for l in range(n-1,-1,-1):
    print(res[l])