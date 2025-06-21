m, d = map(int, input().split())
cnt = 0
for i in range(1, m + 1):
    for j in range(22, d + 1):
        s = str(j)
        if int(s[0]) >= 2 and int(s[1]) >= 2 and i == int(s[0]) * int(s[1]):
            cnt += 1
print(cnt)