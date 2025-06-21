N, M = map(int, input().split())
X = sorted(map(int, input().split()))

d = [0] * (M - 1)

if (N >= M):
    print(0)
    exit()
else:
    for i in range(M):
        if (i == M - 1):
            break
        else:
            d[i] = X[i + 1] - X[i]

d.sort(reverse=True)
count = 0
for i in d:
    if (N > 1):
        N -= 1
        continue
    elif(N == 1):
        count += i

print(count)
