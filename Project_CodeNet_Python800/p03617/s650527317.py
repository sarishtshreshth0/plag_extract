q, h, s, d = map(int, input().split())
n = int(input())
a = [8*q, 4*h, 2*s, d]
b = [4*q, 2*h, s]

price = min(a) * (n // 2) + min(b) * (n % 2)

print(price)