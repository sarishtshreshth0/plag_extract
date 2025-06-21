n, x = list(map(int, input().split()))
xi = list(map(int, input().split()))

xi = [abs(xval - x) for xval in xi]

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

res = xi[0]
for i in range(1, len(xi)):
    res = gcd(res, xi[i])

print(res)