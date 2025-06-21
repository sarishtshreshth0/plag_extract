M, D = map(int, input().split())
count = 0

for i in range(1, M+1):
    for j in range(22, D+1):
        s = str(j)
        if int(s[1]) >= 2 and int(s[0]) * int(s[1]) == i:
            count += 1

print(count)