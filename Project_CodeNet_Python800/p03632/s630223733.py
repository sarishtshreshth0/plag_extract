A,B,C,D = map(int,input().split())

ans=0

if A<C:
    if B<=D:
        ans=B-C
    else:
        ans=D-C
else:
    if B<=D:
        ans=B-A
    else:
        ans=D-A

if ans>=0:
    print(ans)
else:
    print(0)