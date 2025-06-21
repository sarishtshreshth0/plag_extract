q, h, s, d = map(int, input().split())
n = int(input())
one = [q*4, h*2, s]
one.sort()
cost = 0
if one[0]*2>d:
    cost += d*(n//2)
    n %= 2
cost += one[0]*int(n)
n -= int(n)
if n==0:
    print(cost)
else:
    n *= 100
    x = []
    x.append(q*(n//25))
    x.append(s*(n//50)+q*((n%50)//25))
    print(min(x)+cost)