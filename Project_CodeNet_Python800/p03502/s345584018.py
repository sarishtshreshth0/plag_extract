n = input()
list_n = list(n)

fx = 0
for i in list_n:
  fx += int(i)

if int(n)%fx == 0:
  print("Yes")
else :
  print("No")