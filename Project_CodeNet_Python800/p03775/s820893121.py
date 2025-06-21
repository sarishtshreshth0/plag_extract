N = int(input())

ans = 9999
m = 1
while m*m <= N:
    if N%m==0:
        a = len(str(m))
        b = len(str(N//m))
        ans = min(ans, max(a,b))
    m += 1

print(ans)