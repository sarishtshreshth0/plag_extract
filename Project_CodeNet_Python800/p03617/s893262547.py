q, h, s, d = map(int,input().split())
n = int(input())
s = min(4*q, 2*h, s)
if 2*s > d:
    if n%2 == 0:
        ans = n//2 * d
    else:
        ans = n//2 * d + s
else:
    ans = n * s
print(ans)