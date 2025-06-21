a, b = [int(x) for x in input().split()]
if a == b:
    ans = "Draw"
elif a == 1 or (a > b >= 2):
    ans = "Alice"
elif b == 1 or (b > a >= 2):
    ans = "Bob"
print(ans)