# A - Multiple of 2 and N

N = int(input())

def gcd(x, y):
    if x == 0:
        return y
    else:
        return gcd(y%x, x)

print((2 * N) // gcd(2, N))