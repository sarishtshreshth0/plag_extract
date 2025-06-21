N = int(input())

if N == 1:
    print(1)
    exit()

ans = 10**12
for i in range(1, N):
    if i * i > N:
        break
    if N % i == 0:
        F = max(len(str(i)), len(str(N // i)))
        ans = min(ans, F)
print(ans)
