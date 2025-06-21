a,b,c,d = map(int,input().split(" "))

if a <= c < b:
    print(min(b,d)-c)
elif c <= a < d:
    print(min(d,b)-a)
else:
    print(0)