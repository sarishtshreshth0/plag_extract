N=int(input())
answer=[3,5,7]
for i in range(8):
  A=[i*10+3 for i in answer]
  C=[i*10+5 for i in answer]
  B=[i*10+7 for i in answer]
  answer.extend(A)
  answer.extend(B)
  answer.extend(C)
s=0
answer=list(set(answer))
for i in answer:
  if i<=N:
    if set(str(i))=={"3","5","7"}:
      s+=1
print(s)