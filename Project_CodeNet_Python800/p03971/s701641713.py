n,a,b = map(int,input().split())
s = input()
na = 0
nb = 0
for i in range(len(s)):
  if na + nb >= a+b:
    print("No")
  elif s[i]=="a":
    na += 1
    print("Yes")
  elif s[i]=="b":
    if nb < b:
      nb += 1
      print("Yes")
    else:
      print("No")
  else:
    print("No")