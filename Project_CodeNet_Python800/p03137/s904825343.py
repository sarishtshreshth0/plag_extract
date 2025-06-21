n,m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
if m == 1:
    print(0)
else:
    u = [0] * (100000)
    for i in range(m-1):
        u[i] = x[i+1]-x[i]
    u.sort(reverse=True)
    c = 0
    for i in range(n-1):
        c += u[i]
    print(sum(u)-c)