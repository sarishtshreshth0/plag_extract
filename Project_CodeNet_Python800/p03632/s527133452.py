a,b,c,d = map(int,input().split())
if b<=c or d<=a:
    print(0)
else:
    left = max(a,c)
    right = min(b,d)
    print(right-left)