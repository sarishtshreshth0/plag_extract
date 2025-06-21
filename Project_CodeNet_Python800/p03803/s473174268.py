def checkCard(x, y):
  if x == 1 and y == 13:
    return "Alice"
  elif x == 13 and y == 1:
    return "Bob"
  elif x == 1 and y == 1:
    return "Draw"
  else:
    return ""

a, b = map(int, input().split())
result = checkCard(a,b)
if result == "":
  if a > b:
    print("Alice")
  elif a == b:
    print("Draw")
  else:
    print("Bob")
    
else:
  print(result)