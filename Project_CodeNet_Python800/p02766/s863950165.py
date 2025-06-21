N, K = map(int, input().split())
ans = 0

for i in range(1,N+1):
    if N < K**i:
        ans = i
        break

print(ans)