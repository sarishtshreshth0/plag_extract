def resolve():
    import math
    n=int(input())
    d=list(map(int,input().split()))
    d2=[0]*n
    c=1
    for m in d:
        d2[m]+=1

    # print(d2)
    for i in range(1,n):
        c=c* pow(d2[i-1],d2[i],998244353)

    if d2[0]>1 or d[0]!=0:
        print(0)
    else:
        print(c % 998244353)
resolve()