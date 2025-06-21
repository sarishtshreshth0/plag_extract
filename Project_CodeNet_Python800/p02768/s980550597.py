N, a, b = list(map(int, input().split()))
p = 10 ** 9 + 7

factinv = [1, 1]
inv = [0, 1]

for i in range(2, 10**6):
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

def comb(n, k):
    cmb = 1
    for i in range(n-k+1, n+1):
        cmb = cmb * i % p
    return cmb * factinv[k]


print(((2 ** N - 1) % p - comb(N, a) % p - comb(N, b) % p) % p)
