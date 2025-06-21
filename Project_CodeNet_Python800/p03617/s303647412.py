a, b, c, d = map(int, input().split())
n = int(input())
 
b = min(a + a, b)
c = min(b + b, c)
d = min(c + c, d)
 
q, r = divmod(n, 2)
x = q * d + r * c
print(x)