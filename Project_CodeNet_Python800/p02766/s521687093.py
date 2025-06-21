s, k = map(int,input().split())
c = []
while s > 0:
    a = s % k
    c.append(a)
    s //= k

print(len(c))
