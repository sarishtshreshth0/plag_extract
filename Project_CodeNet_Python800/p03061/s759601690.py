def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
n = int(input())
A = list(map(int, input().split()))
L = [0]*n
R = [0]*n
for i in range(n-1):
    R [i+1] = gcd(R[i], A[i])
    L[i+1] = gcd(L[i], A[-i-1])
print(max(gcd(R[i], L[-i-1]) for i in range(n)))