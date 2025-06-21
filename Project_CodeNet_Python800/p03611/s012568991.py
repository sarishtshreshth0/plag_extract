N = int(input())
a = list(map(int,input().split()))
b = [0]*(10**5+10)
for e in a:
    b[e+1] += 1
ans = 0
for k in range(10**5+2):
    ans = max(ans,b[k]+b[k+1]+b[k+2])
print(ans)
