a,b = map(int, input().split())
ans = "Bob"
if a < b:
    if a == 1: ans = "Alice"
elif a > b:
    if b != 1: ans = "Alice"
elif a == b:
    ans = "Draw"
print(ans)