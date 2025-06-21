import string

a, b = map(int, input().split())
s = list(input())
flag = True
hyphen_count = s.count("-")

if "-" in s and hyphen_count == 1:
  hyphen_position = s.index("-")
  
  for i in range(len(s)):
    if not s[i] in string.digits and i != hyphen_position:
      flag = False
    elif a != len(s[0:hyphen_position]):
      flag = False
    elif b != len(s[hyphen_position + 1:len(s)]):
      flag = False
    
else:
  flag = False

if flag:
  print("Yes")
else:
  print("No")