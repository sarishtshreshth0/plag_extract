def gcd_(a, b):
    if a < b:  a, b = b, a
    if b == 0:  return a
    return gcd_(b, a % b)

def gcd(l):
    ans = l[0]
    for i in l:  ans = gcd_(ans, i)
    return ans

N, X = list(map(int,input().split()))
a = list(map(int,input().split()))
p = [abs(X - a[i]) for i in range(N)]
ans = gcd(p)
print(ans)