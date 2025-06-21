N = int(input())
sqrt = pow(N, 0.5)
ans = 10**10

for i in range(1, int(sqrt)+1):
    if N % i == 0:
        ans = min(ans, len(str(max(i, N//i))))
print(ans)
