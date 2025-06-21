a,b,c = map(int,input().split())
x = sorted([a,b,c])
ans = "No"

if x[1] == c:
    ans = "Yes"
    
print(ans)