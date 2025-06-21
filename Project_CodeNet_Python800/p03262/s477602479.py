n,x = map(int,input().split())
ls = list(map(int,input().split()))
ls = list(map(lambda t:abs(t-x),ls))
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def gcdlist(l):
    a = l[0]
    for i in range(len(l)):
        a = gcd(a,l[i])
    return a
print(gcdlist(ls))