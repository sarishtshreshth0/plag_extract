M,D= list(map(int,input().split()))
ans=0
if D < 10:
   print(0)
   exit()
for i in range(1,M+1):
   for j in range(10,D+1):
      s=str(j)
      if i == int(s[0])*int(s[1]) and int(s[0])>=2 and int(s[1])>=2:
         ans+=1
print(ans)