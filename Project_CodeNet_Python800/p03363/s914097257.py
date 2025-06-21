#累積和　AGC023
from collections import Counter
from math import factorial
def nC2(n):
    if n >= 2:
        return factorial(n) // (factorial(n-2)*factorial(2))
    else:
        return 0
N = int(input())
A = list(map(int,input().split()))
B = [0]
ans = 0
for i in range(N):
    B.append(A[i] + B[i])
C =Counter(B)

for v in C.values():
    ans += nC2(v)
print(ans)