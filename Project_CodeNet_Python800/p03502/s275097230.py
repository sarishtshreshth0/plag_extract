n=input()

f=sum([int(_) for _ in n])

#print(f,n)

if int(n)%f==0:
  print("Yes")
else:
  print("No")