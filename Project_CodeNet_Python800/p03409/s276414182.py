n = int(input())
AB = []
for _ in range(n):
    a, b = map(int, input().split())
    AB.append((a,b))

CD = []
for _ in range(n):
    c, d = map(int, input().split())
    CD.append((c,d))

CD = sorted(CD, key=lambda x:x[1])
count = 0

for cd in CD:
    c = cd[0]
    d = cd[1]
    max_a = -1
    max_b = -1
    for ab in AB:
        a = ab[0]
        b = ab[1]
        if b < d and a < c:
            if max_a < a:
                max_a = a
                max_b = b
    if max_a == -1:
        pass
    else:
        AB.remove((max_a, max_b))
        count += 1

print(count)