H,W=map(int,input().split())

if H%2==0:
    if W%2==0:
        ans=W//2*H
    else:
        ans=H//2*W
else:
    if W%2==0:
        ans=W//2*H
    else:
        ans=(W//2+1)*H-H//2

if H==1 or W==1:
    ans=1
    
print(ans)