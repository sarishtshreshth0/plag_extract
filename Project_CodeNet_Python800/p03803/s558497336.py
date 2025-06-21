a, b = map(int, input().split())
judge = ""
if a == b:
    judge = "Draw"
elif a == 1:
    judge = "Alice"
elif b == 1:
    judge = "Bob"
elif a < b:
    judge = "Bob"
elif a > b:
    judge = "Alice"
else:
    judge = "Draw"

print(judge)