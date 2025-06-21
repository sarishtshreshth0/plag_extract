n,m = map(int,input().split())
x = list(map(int,input().split()))
if n >= m:
    print(0)
    exit(0)

x.sort()
y = []
for i in range(1,m):
    y.append(x[i] - x[i-1])
y.sort(reverse = True)
ans = sum(y)
ans2 = sum(y[:n-1])
print(ans - ans2)