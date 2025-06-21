a,b = map(int,input().split())

p=a-1
if (a-1)%4==0:
  p=a-1
elif (a-1)%4==1:
  p=1
elif (a-1)%4==2:
  p=(a-1)^1
else:
  p=0
  
if b%4==0:
  b=b
elif b%4==1:
  b=1
elif b%4==2:
  b=b^1
else:
  b=0
print(p^b)