N=int(input())
ans=0
for i in range((3**10-1)//2):
 Sui=[0]*9
 for j in range(9):
  if i==0:
   Sui[j]=0
  elif i%3==0:
   Sui[j]=3
   i-=3
  elif i%3==1:
   Sui[j]=5
   i-=1
  else:
   Sui[j]=7
   i-=2
  i=i//3
 if 3 in Sui and 5 in Sui and 7 in Sui:
  b=0
  for j in range(9):
   b+=Sui[j]*(10**j)
  if b<=N:
   ans+=1
print(ans)