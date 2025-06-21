a,b = map(int,input().split())
s = input()
for i in range(a+b+1):
  if i == a:
    if s[i] != "-":
      print("No")
      exit()
  else:
    if s[i] == "-":
      print("No")
      exit()
print("Yes")