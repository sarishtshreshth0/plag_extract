n = int(input())
ls = []
for i in range(n-1):
    c, s, f = map(int, input().split())
    ls.append((c, s, f))

for i in range(n-1):
    x = 0
    for j in range(i, n-1):
        if x < ls[j][1]:
            x = ls[j][1] + ls[j][0]
        else:
            mod = x % ls[j][2]
            if mod == 0:
                time = 0
            else:
                time = ls[j][2] - mod
            x += time + ls[j][0]
    print(x)

print(0)
