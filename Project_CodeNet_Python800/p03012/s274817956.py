N = int(input())

weights = list(map(int,input().split()))

ans = 100*1000

for i in range(N):
    f = sum(weights[:i])
    s = sum(weights[i:])
    dif = abs(f-s)
    
    if dif < ans:
        ans = dif
        
print(ans)