A, B=map(int, input().split())
if A==B:
    print(A)
    exit()

if B - A<=1000:
    ans=A
    for i in range(A+1, B+1):
        ans=ans^i
    print(ans)
else:
    lis=[]
    for i in range(A, B+1):
        if i%4==0:
            break
        else:
            lis.append(i)
    for j in range(B, A-1, -1):
        if j%4==0:
            lis.append(j)
            break
        else:
            lis.append(j)
    for i in range(len(lis)):
        if i==0:
            ans=lis[i]
        else:
            ans=ans^lis[i]
    print(ans)
