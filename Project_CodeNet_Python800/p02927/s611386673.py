m,d = map(int,input().split())
ans = 0
for i in range(22,d+1):
    a = i%10
    b = i//10
    if a>= 2 and b >= 2 and 0 < a*b < m+1:
        ans += 1
        
print(ans)