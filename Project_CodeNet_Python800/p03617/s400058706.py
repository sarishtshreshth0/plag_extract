q, h, s, d = map(int, input().split())
n = int(input())

cst1 = min(s,2*h, 4*q)
cst2 = min(d, 2*cst1)

print(n//2*cst2+n%2*cst1)