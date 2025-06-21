n = int(input())

c, s, f = [], [], []
for _ in range(n-1):
    x,y,z = map(int,input().split())
    c.append(x)
    s.append(y)
    f.append(z)

for i in range(n-1):
    tmp = 0
    for j in range(i, n-1):
        for k in range(10**8):
            if tmp <= s[j] + f[j] * k:
                tmp = s[j] + f[j] * k + c[j]
                break
    else:
        print(tmp)

print(0)
