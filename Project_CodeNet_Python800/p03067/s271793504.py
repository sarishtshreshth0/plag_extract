a,b,c = map(int,input().split())
if a < c < b:
        ans = "Yes"
elif b < c < a:
        ans = "Yes"
else:
        ans = "No"
print(ans)
