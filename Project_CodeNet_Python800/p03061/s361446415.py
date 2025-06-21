def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return a*b // gcd(a,b)

n = int(input())
a = list(map(int,input().split()))
b = a[::-1]
l = [0]
r = [0]
for i in range(n):
    l.append(gcd(a[i],l[-1]))
    r.append(gcd(b[i],r[-1]))
r = r[::-1]
ans = 0
for i in range(n):
    ans = max(ans,gcd(l[i],r[i+1]))
print(ans)