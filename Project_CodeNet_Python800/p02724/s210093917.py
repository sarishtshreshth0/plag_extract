x=int(input())
a=x
i=0
j=0
if 500<= x:
  while i*500<x:
    i+=1
  i-=1
  x-=500*i
if 5<=x:
  while j*5<x:
    j+=1
  j-=1
if i==0 and j==0:
  print(0)
elif a%500==0:
  print(a//500 * 1000)
else:
  print(1000*i+5*j)
