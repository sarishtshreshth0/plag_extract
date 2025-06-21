q, h, s, d = map(int, input().split())
n = int(input())

d = min([q*8, h*4, s*2, d])
s = min([q*4, h*2, s])
ans = (n // 2) * d + (n % 2) * s
print(ans)
