m, d = map(int, input().split())

if d < 10:
    print(0)
    exit()

cnt = 0
for i in range(1,m+1):
    for j in range(10, d+1):
        t = str(j)
        if int(t[1]) >= 2 and int(t[0]) >= 2:
            if int(t[1]) * int(t[0]) == i:
                cnt += 1

print(cnt)

