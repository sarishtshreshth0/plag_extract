a, b, c, d = map(int,input().split())
n = int(input())

#1リットル買う最も安い方法を考える
x = a*4
y = b*2
z = min(x,y,c)
if z == x:
    e = x
elif z == y:
    e = y
else:
    e = c

if e*2 <= d:
    print(e*n)
else:
    if n%2 == 0:
        print(d*n//2)
    else:
        print(d*(n//2)+e)
