N, X = map(int, input().split())
A = list(map(lambda a: abs(int(a) - X), input().split()))
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
g = A[0]
for a in A[1:]:
    g = gcd(g, a)
print(g)
