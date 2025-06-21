N = int(input())
a = list(map(int,input().split()))

lst = [0]*(N-1)
x = [a[0]]*(N-1)
y = [sum(a)-a[0]]*(N-1)
lst[0] = abs(x[0]-y[0])

for i in range(1,N-1):
    x[i] = x[i-1]+a[i]
    y[i] = y[i-1]-a[i]
    lst[i] = abs(x[i]-y[i])

ans = min(lst)
print(ans)
