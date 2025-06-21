n=int(input())
m=n
wa=0
while m:
  wa+=m%10
  m//=10
  
if n%wa==0:print("Yes")
else:print("No")