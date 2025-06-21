n, k  =  map(int,input().split())

if n == 1:
    print(1)
else:
    a=1
    ans = 0
    while a<=n:
        a *=k
        ans += 1

    print(ans)
