q,h,s,d = [int(x) for x in input().split()]
n = int(input())

print((n//2) * min(8*q, 4*h, 2*s, d) + (n%2) * min(4*q, 2*h, s))