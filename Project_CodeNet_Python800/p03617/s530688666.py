q,h,s,d = map(int,input().split())
n = int(input())
s = min(s,min(q*2,h)*2)
if s*2<d:
    print(n*s)
else:
    if n%2==0:
        print((n//2)*d)
    else:
        print((n//2)*d+s)