N, K = map(int, input().split())

n = 0
x = 0

while True:
    x = K**n
    if x > N:
        n -= 1
        break
    n += 1

ans = []

for i in range(n, -1, -1):
    if K**i < N:
        ans.append(N//(K**i))
        N = N % (K**i)
    else:
        ans.append(0)

print(len(ans))
