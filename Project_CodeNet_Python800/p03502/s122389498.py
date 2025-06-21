N = int(input())
M = N*1
a = 0
while N > 0:
  a += N%10
  N //= 10
if M%a == 0:
  print("Yes")
else:
  print("No")