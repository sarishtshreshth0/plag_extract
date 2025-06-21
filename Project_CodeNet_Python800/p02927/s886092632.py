n,m=input().split()
if int(m)>=10:
    ans=0
    for i in range(4,int(n)+1):
      for j in range(2,int(m[0])):
        for k in range(2,10):
          if i==j*k:
            ans+=1
    for i in range(4,int(n)+1):
      for j in range(2,int(m[1])+1):
          if i==j*int(m[0]):
            ans+=1
    print(ans)
else:
  print(0)