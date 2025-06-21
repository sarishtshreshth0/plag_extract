q,h,s,d = map(int, input().split())
n = int(input())

if q*2 < h: h = q*2
if h*2 < s: s = h*2
if s*2 < d: d = s*2

ans = n//2*d
n -= n//2 * 2
ans += n*s
print(ans)