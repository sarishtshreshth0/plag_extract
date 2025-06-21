n, s = map(int, input().split())
x = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

diff = []

for i in x:
    diff.append(abs(i-s))

ans = diff[0]
for i in diff:
    ans = (gcd(ans, i))

print(ans)