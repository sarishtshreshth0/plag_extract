n,a,b = map(int,input().split())
pas,foreignpass = 0,0
s = input()
for i in range (n):
  if pas == a+b:
    print("No")
  elif s[i] == "c":
    print("No")
    continue
  elif s[i] == "a":
    pas += 1
    print("Yes")
  elif s[i] == "b" and foreignpass < b:
    pas += 1
    print("Yes")
    foreignpass += 1
  else:
    print("No")
    continue