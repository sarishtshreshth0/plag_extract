a,b,c,d=map(int,input().split())
#a b
#c d

if b>=c and d>=a:
    print((min(b,d)-max(a,c)))
else:
    print(0)
