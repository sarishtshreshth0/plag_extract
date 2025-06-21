N = int(input())
n = N
sum = 0
while N > 0:
  sum += N%10
  N = int(N/10)

if (n%sum) == 0:
  print('Yes')
else:
  print('No')