N = int(input())

ans = 999999
m = 1
while m*m <= N:
    if N%m == 0:
        n = N//m
        t = max(len(str(n)), len(str(m)))
        ans = min(ans, t)
    m += 1
print(ans)