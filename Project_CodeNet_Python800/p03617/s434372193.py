q,h,s,d = map(int, input().split())
n = int(input())

two = min(8*q, 4*h, 2*s, d)
one = min(4*q, 2*h, s)
x = n // 2 * two
x += (n % 2) * one
print(x)