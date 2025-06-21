n,m = map(int,input().split())
n = min(n,m)
x = sorted(map(int,input().split()))
dx = [0] * (m-1)

for i in range(m-1):
    dx[i] = x[i+1] - x[i]
    
dx = sorted(dx)[::-1]
    
print(x[-1] - x[0] - sum(dx[:n-1]))