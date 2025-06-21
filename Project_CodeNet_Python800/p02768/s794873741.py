def power(n,p,m):
    if p == 0:
        return 1
    elif p%2:
        return (power(n,p-1,m)*n)%m
    else:
        return ((power(n,p//2,m))**2)%m

def choose(n,t,m):
    x, y = 1, 1
    for i in range(t):
        x = x * (n - i) % m
        y = y * (i + 1) % m
    return x * power(y,m-2,m) % m


m = 10**9+7
n,a,b = map(int,input().split())


flower = (power(2,n,m)-1) - choose(n,a,m) - choose(n,b,m)
while flower < 0:
    flower += m

print(flower)