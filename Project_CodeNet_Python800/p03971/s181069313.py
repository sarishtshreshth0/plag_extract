n,a,b = map(int,input().split())
li = list(input())
c=a+b
for stu in li:
  if stu=='a':
    if c==0:
      print("No")
    else:
      c-=1
      print("Yes")
  elif stu=='b':
    if b==0 or c==0:
      print("No")
    else:
      c-=1
      b-=1
      print("Yes")
  else:
    print("No")