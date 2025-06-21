a,b,c,d = map(int,input().split())

c = min(b,d) - max(a,c)
if c > 0:
    print(c)

else:
    print(0)
