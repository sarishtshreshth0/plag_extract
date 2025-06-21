N, D = map(int, input().split())
X = [tuple(map(int, input().split())) for _ in range(N)]
r = 0
for p in X:
    for q in X:
        if p != q:
            d = sum([(x-y)**2 for x, y in zip(p, q)])**(0.5)
            if int(d) == d:
                r += 1
print(r//2)
