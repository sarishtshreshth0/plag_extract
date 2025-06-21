n, X = map(int, input().split())
x = list(map(abs, [i-X for i in list(map(int, input().split()))]))
x.sort()
if x[0] == 0:
    del x[0]
    n -= 1
def gcd(a, b):
    while True:
        c = a%b
        if c == 0:
            break
        a = b
        b = c
    return b

if n == 1:
    ans = x[0]
else:
    for i in range(1, n):
        x[i] = gcd(x[i], x[i - 1])
    ans = x[-1]
print(ans)