n,m = map(int,input().split())
n=min(n,m)
x = list(map(int,input().split()))

x = sorted(x)

#print("x",x)

y = []

for i in range(m-1):
    y.append(x[i+1]-x[i])

y = sorted(y, reverse=True)

#print("y",y)

skip = 0
for i in range(n-1):
    skip += y[i]

print(max(x)-min(x)-skip)
