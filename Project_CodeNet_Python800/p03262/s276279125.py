import numpy as np

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b)


N, X = map(int, input().split())
x = list(map(int, input().split()))

s = np.array(x)
s = abs(s-X)

if len(s) == 1:
    print(s[0])
    exit()

for i in range(1, len(s)):
    if i == 1:
        D = gcd(s[i],s[i-1])
    D = gcd(s[i], D)

print(D)
