M,D = map(int, input().split())


def seki(n):
    s = str(n)
    i1,i2 = int(s[0]), int(s[1])
    if i1>=2 and i2>=2:
        return i1*i2
    else:
        return -1

res = 0
for m in range(1,M+1):
    for d in range(11,D+1):
        if m==seki(d):
            res += 1
print(res)

