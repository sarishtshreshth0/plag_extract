n = int(input()); a = list(map(int, input().split()))
b = [0]; c = {}
for i in range(n): b.append(b[-1]+a[i])
for i in range(n+1):
    if b[i] in c: c[b[i]] += 1
    else: c[b[i]] = 1
d = list(c.values()); x = 0
for i in range(len(d)): x += d[i]*(d[i]-1)//2
print(x)