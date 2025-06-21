q, h, s, d = map(int, input().split())
n = int(input())

ans = 0

s = min(s, 2*min(h, 2*q))

if s*2 <= d:
    ans = s*n
elif s*2 > d:
    ans = n//2*d + n%2*s

print(ans)