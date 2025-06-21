A,B=map(int,input().split())
ans=0
if A%2==0:
    if B%2==0:
        a=B-A
        a=a//2
        a=a%2
        if a==1:
            print(B+1)
        else:
            print(B)
    else:
        a=B-A+1
        a=a//2
        if a%2==0:
            print(0)
        else:
            print(1)
else:
    if B%2==1:
        a=B-A
        a=a//2
        if a%2==0:
            print(A)
        else:
            print(A-1)
    else:
        a=B-A-1
        a=a//2
        if a%2==1:
            A=A-1
        for i in range(60):
            a1=A%2
            b1=B%2
            ans+=((a1+b1)%2)*2**(i)
            A=A//2
            B=B//2
        print(ans)