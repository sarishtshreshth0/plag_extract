q,h,s,d=map(int,input().split())
n=int(input())
a=sorted([q*8,h*4,s*2,d])
if a[0]==q*8:
    print(q*4*n)
elif a[0]==h*4:
    print(h*2*n)
elif a[0]==s*2:
    print(s*n)
else:
    if n%2==0:
        print(d*(n//2))
    else:
        ans=d*(n//2)
        a=sorted([q*8,h*4,s*2])
        if a[0]==q*8:
            ans+=q*4
        elif a[0]==h*4:
            ans+=h*2
        else:
            ans+=s
        print(ans)