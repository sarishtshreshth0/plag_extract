n, m = list(map(int, input().split()))
x = list(map(int, input().split()))

s = 0

if n >= m:
    s = 0
else:
    x.sort()
    d = []
    for j in range(m-1):
        d.append(x[j+1]-x[j])
    d.sort()
    s = sum(d[:m-n])

print(s)