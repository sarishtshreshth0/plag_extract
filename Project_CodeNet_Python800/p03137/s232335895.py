n, m = map(int, input().split())
x = list(map(int, input().split()))

if n >= m:
    ans = 0
else:
    x.sort()
    kyori = [x[i]-x[i-1] for i in range(1,m)]
    kyori.sort()
    ans = sum(kyori[0:m-n])
print(ans)
