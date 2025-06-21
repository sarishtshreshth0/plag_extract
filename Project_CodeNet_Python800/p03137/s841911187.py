n,m = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
y=[abs(x[i]-x[i+1]) for i in range(m-1)]
y.sort(reverse=1)
print(sum(y[n-1:]))