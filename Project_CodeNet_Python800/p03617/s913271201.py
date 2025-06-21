q, h, s, d = map(int, input().split())
n = int(input())
m = 0
l = [q, min(q*2, h), min(q*4, h*2, s), min(q*8, h*4, s*2, d)]

m += (n // 2) * l[3] + (n % 2) * l[2]

print(int(m))