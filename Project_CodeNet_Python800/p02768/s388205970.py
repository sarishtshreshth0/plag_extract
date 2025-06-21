import math

n, a, b = list(map(int, input().split()))

MOD = int(1e9) + 7

s = pow(2, n, MOD)-1

def cbn(n, a, MOD):
    x = 1
    for i in range(a):
        x = (x * (n-i)) % MOD

    y = math.factorial(a) % MOD
    return x * pow(y, MOD-2, MOD) %MOD

s = (s- cbn(n, a, MOD)) %MOD
s = (s- cbn(n, b, MOD)) %MOD


print(s)