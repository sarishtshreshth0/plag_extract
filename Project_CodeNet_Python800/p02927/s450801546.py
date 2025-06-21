m,d = map(int,input().split())

x=0

for a in range(1,m+1):
  for b in range(22,d+1):
#    print(a,b)
    if (a==(b//10)*(b%10)) and (b%10!=1):
      x+=1
#      print("hit!")
#      print(a,b)
print(x)