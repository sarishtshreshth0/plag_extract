a, b = map(int, input().split()) 
if a == b: 
  ans = "Draw"
elif a == 1 or (b != 1 and a > b):
  ans = "Alice"
elif b == 1 or (a != 1 and a < b):
  ans = "Bob"

print(ans)