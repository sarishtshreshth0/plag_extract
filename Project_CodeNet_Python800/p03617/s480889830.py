q, h, s, d = map(int, input().split())
n = int(input())

l = min(4*q, 2*h, s)
l_2 = min(2*l, d)

print((n//2) * l_2 + (n%2) * l)