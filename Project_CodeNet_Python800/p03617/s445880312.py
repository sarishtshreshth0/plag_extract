q, h, s, d = map(int, input().split())
n = int(input())

h = min(q*2,h)
s = min(h*2,s)
if 2*s >= d:
    a,b = n//2, n%2
    print(a*d+b*s)
else:
    print(n*s)
