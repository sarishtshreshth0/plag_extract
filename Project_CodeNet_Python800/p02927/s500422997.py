M, D = map(int, input().split())
count = 0
for i in range(1, M+1):
    for j in range(1, D+1):
        d_s = str(j)
        if len(d_s) == 1 or int(d_s[0]) < 2 or int(d_s[1]) < 2:
            continue
        elif i == int(d_s[0])*int(d_s[1]):
            count += 1
print(count)