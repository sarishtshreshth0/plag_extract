a, b = map(int, input().split())

def f(a):
    if a <= 200:
        rv = 0
        for i in range(a + 1):
            rv ^= i
        return rv
    d = 1
    while d <= a:
        d <<= 1
    d >>= 1
    return (0 if a & 1 else d) | f(a - d)

print(f(b) ^ f(a-1))
