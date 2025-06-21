n,m = map(int,input().split())
x = list(map(int,input().split()))
x = sorted(x)
s = [0]*m
for i in range(1,m):
    s[i] = x[i] - x[i-1]
s = sorted(s)
if n < m:
    print(sum(s[:m-n+1]))
else:
    print(0)