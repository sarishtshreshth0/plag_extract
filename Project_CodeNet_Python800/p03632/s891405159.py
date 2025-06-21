a,b,c,d = map(int,input().split())

if a < c:
    s = c
else:
    s = a

if b < d:
    e = b
else:
    e = d

print (max(e-s,0))
