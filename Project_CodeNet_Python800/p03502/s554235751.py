n=int(input())
m=n
sum_digit=0
while n>0:
  sum_digit+=n%10
  n=n//10
if m%sum_digit==0:
  print("Yes")
else:
  print("No")