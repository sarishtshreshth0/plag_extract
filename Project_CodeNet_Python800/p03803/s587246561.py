A, B = map(int, input().split())
a, b, d = 'Alice', 'Bob', 'Draw'
if A == 1:
    A = 14
if B == 1:
    B = 14

if A > B:
    ans = a
elif A < B:
    ans = b
else:
    ans = d

print(ans)