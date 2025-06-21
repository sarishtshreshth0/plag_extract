_input = input().split(" ")
_A = int(_input[0])
_B = int(_input[1])
_C = int(_input[2])

if _A < _B:
  if _A < _C and _C < _B:
    print("Yes")
  else:
    print("No")
else:
  if _B < _C and _C < _A:
    print("Yes")
  else:
    print("No")