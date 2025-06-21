a, b = map(int, input().split())

ans = str()
if a == 1 or b == 1:
    if a == 1 and b == 1:
        ans = "Draw"
    elif a == 1:
        ans = "Alice"
    elif b == 1:
        ans = "Bob"
else:
    if a > b:
        ans = "Alice"
    elif b > a:
        ans = "Bob"
    else:
        ans = "Draw"

print(ans)