import fractions
def GCD(a, b):
    if a * b == 0:
        return a + b
    return fractions.gcd(a, b)

n = int(input())
a = list(map(int,input().split()))

L = [0] * n
R = [0] * n

for i in range(n - 1):
    L[i + 1] = GCD(a[i], L[i])
    R[-(i + 2)] = GCD(a[-(i + 1)], R[-(i + 1)])

M = [0] * n
for i in range(n):
    M[i] = GCD(L[i], R[i])
print(max(M))