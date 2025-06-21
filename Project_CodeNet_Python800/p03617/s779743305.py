def resolve():
    A,B,C,D = map(int,input().split())
    N = int(input())*4
    cc = [(8*A,A,1),(4*B,B,2),(2*C,C,4),(D,D,8)]
    cc.sort()
    ans = 0

    for _,cost,vol in cc:
         enable = N//vol
         ans += enable*cost
         N %= vol
    print(ans)
resolve()
