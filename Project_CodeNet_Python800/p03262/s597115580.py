from math import gcd

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, X = MI()
x = LI()
D = abs(X - x[0])

for i in range(1, N):
    D = gcd(D, abs(X - x[i]))
    
print(D)