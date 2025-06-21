m, d = map(int, input().split())
cnt = 0
for i in range(4, m + 1):
    for j in range(22, d + 1):
        if int(str(j)[0]) > 1 and int(
                str(j)[1]) > 1 and i == int(str(j)[0]) * int(str(j)[1]):
            cnt += 1
print(cnt)
