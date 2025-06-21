q, h, s, d = map(int, input().split())
n = int(input())

L = min(4*q, 2*h, s)
L2 = min(2*L, d)

print((n//2)*L2 + (n%2)*L)