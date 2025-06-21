a,b=map(int, input().split())
s = input()
for i in range(len(s)):
  if i == a:
    if s[i] != "-":
      print("No")
      break
  else:
    if not "0" <= s[i] <= "9":
      print("No")
      break
else:
  print("Yes")