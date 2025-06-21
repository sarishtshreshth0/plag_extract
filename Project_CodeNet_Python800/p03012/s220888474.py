N = int(input())
W = list(map(int, input().split()))

ans = 10**5
for i in range(N-1):
    a = sum(W[:i + 1])
    b = sum(W[i + 1:])
    if abs(a-b) < ans:
        ans = abs(a-b)
print(ans)
