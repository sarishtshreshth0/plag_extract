a,b,c,d=map(int,input().split())
left=max(a,c)
right=min(b,d)
ans = right-left
if ans < 0:
    print(0)
else:
    print(ans)