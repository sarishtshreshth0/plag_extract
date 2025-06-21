M,D = list(map(int, input().strip().split()))
count = 0
for m in range(2,M+1):
    for d in range(22, D+1):
        if ((d%10) >= 2) and (int(d/10) >= 2) and (m == int(d/10) * (d%10)):
            count+=1
print(count)
