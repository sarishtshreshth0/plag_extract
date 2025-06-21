q,h,s,d = map(int, input().split())
n = int(input())

if 2*q < h: h = 2*q
if h*2 < s: s = h*2
if s*2 < d: d = s*2

print(n//2*d + n%2*s)