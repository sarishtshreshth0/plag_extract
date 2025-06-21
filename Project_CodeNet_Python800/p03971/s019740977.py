n,a,b = map(int,input().split())
S = input()
passed = 0
f_passed = 0
for s in S:
  if s == "a":
    if passed < a + b:
      print("Yes")
      passed += 1
    else:
      print("No")
  elif s == "b":
    if passed < a + b and f_passed + 1 <= b:
      print("Yes")
      passed += 1
      f_passed += 1
    else:
      print("No")
  else:
    print("No")
