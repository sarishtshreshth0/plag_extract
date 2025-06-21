Alice, Bob = map(int, input().split())
if Alice == 1 and Bob == 1:
  print("Draw")
elif Alice == 1 and Bob != 1:
  print("Alice")
elif Alice != 1 and Bob == 1:
  print("Bob")
elif Alice > Bob:
  print("Alice")
elif Alice == Bob:
  print("Draw")
else:
  print("Bob")