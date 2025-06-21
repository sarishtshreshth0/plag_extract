M, D = map(int, input().split())
ans = 0
for i in range(22,D+1):
    if 0<(i%10)*(i//10)<=M:
        if i%10>=2 and i//10>=2:
            ans+=1
print(ans)