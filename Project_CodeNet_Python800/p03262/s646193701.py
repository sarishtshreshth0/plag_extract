import math
N, X = map(int, input().split())
arr = list(map(int, input().split()))

kyori = []

for i in arr:
    kyori.append(abs(X-i))

c =math.gcd(kyori[0],kyori[0])
for i in kyori:
    c =math.gcd(c,i)

print(c)




