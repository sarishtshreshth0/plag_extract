n_original =  int(input())
n = n_original
sum = 0
while n//10 != 0:
  sum += n%10
  n = n//10
sum += n
if n_original%sum==0:
  print('Yes')
else:
  print('No')