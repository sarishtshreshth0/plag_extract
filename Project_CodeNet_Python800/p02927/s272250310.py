m, d = map(int, input().split())
r = 0
for mi in range(1, m + 1):
    for di in range(10, d + 1):
        if mi == int(str(di)[0]) * int(str(di)[1]) and int(str(di)[0]) > 1 and int(str(di)[1]) > 1:
            r += 1
print(r)
