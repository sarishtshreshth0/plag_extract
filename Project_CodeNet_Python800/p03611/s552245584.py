n=int(input())
A=list(map(int,input().split()))

count=[0 for _ in range(max(A)+1)]
for i in range(n):
  count[A[i]]+=1
  
answer=0
if n>3:
  for i in range(0,n-2):
    tmp=sum(count[i:i+3])
    if tmp>answer:
      answer=tmp
elif n==2:
  if len(count)>3:
    answer=1
  else:
    answer=2
elif n==1:
  answer=1

print(answer)