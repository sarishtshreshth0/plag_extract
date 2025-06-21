N = int(input())

def sumsum(n):
  flag = True
  res = 0
  while flag:
    res += n % 10
    n = n //10
    if n == 0:
      flag = False
  return res

nn = sumsum(N)
if N % nn == 0:
  print("Yes")
else:
  print("No")