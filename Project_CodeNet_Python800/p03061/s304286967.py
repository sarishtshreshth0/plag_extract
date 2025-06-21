n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

l = [None]*n
r = [None]*n
tmp = 0
for i in range(n):
    tmp = gcd(tmp, a[i])
    l[i] = tmp
tmp = 0
for i in range(n-1, -1, -1):
    tmp = gcd(tmp, a[i])
    r[i] = tmp
ans = max(l[-2], r[1])
for i in range(n-2):
    ans = max(ans, gcd(l[i], r[i+2]))
print(ans)