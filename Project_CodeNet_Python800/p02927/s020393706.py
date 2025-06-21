M,D = map(int,input().split())
res = 0
for i in range(1,M+1):
    for j in range(1,D+1):
        d1 = j % 10
        d10 = j //10
        if 2 <= d1 and 2 <= d10 and d1*d10 == i:
            res += 1
print(res)