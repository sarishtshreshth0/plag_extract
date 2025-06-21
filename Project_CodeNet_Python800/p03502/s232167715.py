def digsum(x):
  ldigit = list(x)
  idigit = [int(n) for n in ldigit]
  return sum(idigit)

N = input()

if(int(N) % digsum(N) == 0):
  print("Yes")
else:
  print("No")