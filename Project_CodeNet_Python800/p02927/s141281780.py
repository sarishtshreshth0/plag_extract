m,d=map(int,input().split())
cnt = 0
for d in range(21,d+1):
    if d%10 >= 2:
        if (d%10) * (d//10) <= m:
            cnt += 1
print(cnt)
