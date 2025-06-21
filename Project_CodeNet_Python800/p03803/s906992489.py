A, B = map(int, input().split())
if A == 1 and B == 13:
    winner = "Alice"
elif A == 13 and B == 1:
    winner = "Bob"
elif A > B:
    winner = "Alice"
elif A < B:
    winner = "Bob"
else:
    winner = "Draw"
print(winner)