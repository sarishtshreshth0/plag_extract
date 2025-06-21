M, D= map(int, input().split())


count = 0
for m in range(1,M+1):
    for d in range(1,D+1):
        if len(str(d)) < 2:
            continue
        if int(str(d)[0]) >= 2 and int(str(d)[1]) >= 2:
            if m == int(str(d)[0]) * int(str(d)[1]):
                count += 1

print(count)