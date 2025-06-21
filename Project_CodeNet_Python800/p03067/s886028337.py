a,b,c=map(int,input().split())
a,b=min(a,b),max(a,b)
if a<=c<=b:
    print("Yes")
else:
    print("No")