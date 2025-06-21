m,d = (int(i) for i in input().split())
ans = 0
for i in range(4,m+1):
    for j in range(22,d+1):
        x,y = j%10,j//10
        if x>1 and y>1 and i==x*y: ans+=1
print(ans)