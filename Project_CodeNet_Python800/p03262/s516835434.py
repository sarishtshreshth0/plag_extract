N, X = map(int, input().split())
x = list(map(int, input().split()))

is_ok = True
# x[i] - X たちの最大公約数

from fractions import gcd
if N == 1:
    print(abs(x[0]-X))
elif N == 2:
    GCD = gcd(abs(x[0]-X), abs(x[1]-X))
    print(GCD)
else:
    GCD = gcd(abs(x[0]-X), abs(x[1]-X))
    for i in range(2, N):
        a = abs(x[i] - X)
        GCD = gcd(GCD, a)

    print(GCD)