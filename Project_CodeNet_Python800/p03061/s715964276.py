from math import gcd
n = int(input())
A = [0] + list(map(int, input().split())) + [0]
n += 2

L, R = [0]*n, [0]*n
gl, gr = 0, 0
for i in range(n):
    gl = gcd(gl, A[i])
    gr = gcd(gr, A[n-i-1])
    L[i] = gl
    R[n-i-1] = gr

ans = L[-1]
for i in range(n-2):
    ans = max(ans, gcd(L[i], R[i+2]))
print(ans)