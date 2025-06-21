a,b = map(int,input().split())
ans = ""
if a == b:
    ans = "Draw"
elif a == 1 or b == 1:
    if a < b:
        ans = "Alice"
    else:
        ans = "Bob"
else:
    if a > b:
        ans = "Alice"
    else:
        ans = "Bob"
print(ans)