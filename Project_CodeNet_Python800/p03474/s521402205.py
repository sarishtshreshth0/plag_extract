a, b = map(int, input().split())
s = input()

x = s[:a].isdecimal()
if s[a] == "-":
  y = True
else:
  y = False
z = s[a+1:].isdecimal()

if x and y and z == True:
  print("Yes")
else:
  print("No")