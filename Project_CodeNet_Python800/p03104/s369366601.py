A,B=map(int,input().split())

if A==0:
    n=(B+1)//2
    if n%2==0:
        if B%2==0:
            print(B)
        else:
            print(0)
    else:
        if B%2==0:
            print(1^B)
        else:
            print(1)
else:
    m=A//2
    if m%2==0:
        if (A-1)%2==0:
            a=A-1
        else:
            a=0
    else:
        if (A-1)%2==0:
            a=1^(A-1)
        else:
            a=1
    n=(B+1)//2
    if n%2==0:
        if B%2==0:
            b=B
        else:
            b=0
    else:
        if B%2==0:
            b=1^B
        else:
            b=1
    ans=a^b
    print(ans)