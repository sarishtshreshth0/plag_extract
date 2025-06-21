n,a,b=map(int, input().split())
s=list(input())
num=0
num_f=0
qual=[]
for i in range(n):
  if num<a+b:
    if s[i]=='a':
      num+=1
      qual.append('Yes')     
    elif s[i]=='b' and num_f<b:
      num+=1
      num_f+=1
      qual.append('Yes')
    else:
      qual.append('No')   
  else:
    qual.append('No')
for i in range(n):
  print(qual[i])