N = int(input())
N_sum = 0
n = N
while n > 0:
  N_sum += n % 10
  n //= 10
if N % N_sum == 0 :
  print("Yes")
else:
  print("No")