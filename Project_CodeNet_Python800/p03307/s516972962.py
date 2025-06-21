def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
print(2*n//gcd(2, n))