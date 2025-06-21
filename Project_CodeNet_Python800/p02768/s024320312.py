
mod = (10 ** 9 + 7)

def comb(n, r):
    p, q = 1, 1

    for i in range(r):
        p = p *(n-i)%mod
        q = q *(i+1)%mod
    
    return p * pow(q, mod-2, mod) % mod


n, a, b = list(map(int, input().split()))

s = pow(2, n, mod) - 1

print((s - comb(n, a) - comb(n, b)) % mod)