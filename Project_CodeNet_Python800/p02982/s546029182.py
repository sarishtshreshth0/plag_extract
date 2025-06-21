n, d = map(int, input().split())
x = list(list(map(int, input().split())) for _ in range(n))

ans = 0
for i in range(len(x)):
    for j in range(i+1, len(x)):
        dist = sum((x-y)**2 for x, y in zip(x[i], x[j]))**0.5
        if dist.is_integer(): ans += 1

print(ans)


