M = 10**9 + 7
n,a,b = map(int, input().split())

def modinv(n):
    return pow(n, M-2, M)

def comb(n, r):
    num = 1
    for i in range(n,n-r,-1):
        cur = i
        while cur%M == 0:
            cur //= M
        num = (num*cur)%M

    denom = 1
    for i in range(1,r+1):
        cur = i
        while cur%M == 0:
            cur //= M
        denom = (denom*cur)%M

    return num * modinv(denom) % M


print((pow(2, n, M) - comb(n, a) - comb(n, b) - 1) % M)