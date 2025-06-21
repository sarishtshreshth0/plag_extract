n,a,b = map(int,input().split())
s = input()
maxa = a+b
maxb = b
counta = 0
countb = 0
for i in range(n):
  if s[i] == 'c':
    print("No")
  elif s[i] == 'b':
    if countb < maxb and counta < maxa:
      print("Yes")
      counta += 1
      countb += 1
    elif counta < maxa:
      print("No")
    else:
      print("No")
  else:
    if counta < maxa:
      print("Yes")
    else:
      print("No")
    counta+=1
