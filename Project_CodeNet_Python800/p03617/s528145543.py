q , h , s , d = map(int,input().split())
n = int(input())
qb = q*8
hb = h*4
sb = s*2
db = d

if min(qb,hb,db,sb) != db:
    print(n*min(q*4,h*2,s))
elif min(qb,hb,db,sb) == db:
    if n % 2 == 0:
        print((n//2)*d)
    elif n % 2 == 1:
        ans = (n//2) * d
        ans += min(q*4,h*2,s)
        print(ans)