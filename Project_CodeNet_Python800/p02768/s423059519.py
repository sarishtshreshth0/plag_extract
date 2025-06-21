M = 10**9 + 7
n,a,b = map(int, input().split())

def modinv(n):
    return pow(n, M-2, M)

def comb(n, r):
    num = denom = 1
    for i in range(1,r+1):
        num = (num*(n+1-i))%M
        denom = (denom*i)%M
    return num * modinv(denom) % M

print((pow(2, n, M) - comb(n, a) - comb(n, b) - 1) % M)