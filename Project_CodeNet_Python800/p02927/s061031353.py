m,d=map(int,input().split())
x=0
if m>=4 and d>=22:
  for i in range(4,m+1):
    for j in range(22,d+1):
      if j%10>1 and int(str(j)[1])*int(str(j)[0])==i:
        x+=1
print(x)