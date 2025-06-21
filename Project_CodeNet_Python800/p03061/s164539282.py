import numpy as np

# 約数列挙(nを含む)
def make_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i)

    return divisors


N = int(input())
A = np.array(input().split(), dtype=np.int64)
A.sort()
A = A[::-1]


p0 = make_divisors(A[0])
p1 = make_divisors(A[-1])
P = p0 | p1

for p in sorted(P)[::-1]:
    c = np.count_nonzero(A % p == 0)
    if c == N - 1:
        break

q = np.gcd.reduce(A)
if p > q:
    print(p)
else:
    print(q)
