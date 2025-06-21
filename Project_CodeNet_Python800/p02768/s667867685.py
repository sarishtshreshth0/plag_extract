n, a, b = map(int, input().split())
M = 10**9 + 7
def cmb(n,r):
    x = 1
    y = 1
    for i in range(r):
        x *= n - i
        x %= M
        y *= (i + 1)
        y %= M
    return x * pow(y, M-2, M) % M

print((pow(2,n,M)-cmb(n,a)-cmb(n,b)-1)%M)