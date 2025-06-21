N = int(input())

ans = float("inf")
for a in range(1, N+1):
    if a * a > N: break
    if N % a ==0:
        b = N / a
        f = max(a, b)
        keta = 0
        while True:
            keta += 1
            if 10 ** keta > f:
                break
        ans = min(ans, keta)
print(ans)
