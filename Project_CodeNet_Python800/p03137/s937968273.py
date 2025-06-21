#ABC117-C
n,m = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
sabun = []
for i in range(1,m):
    sabun.append(x[i]-x[i-1])
sabun.sort(reverse=True)

print(sum(sabun[n-1:]))
