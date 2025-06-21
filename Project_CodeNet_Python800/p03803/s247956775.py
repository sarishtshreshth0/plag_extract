a, b = [int(x) for x in input().split()]
a = 14 if a == 1 else a
b = 14 if b == 1 else b
ans = "Draw"
if a > b:
    ans = "Alice"
elif b > a:
    ans = "Bob"
print(ans)