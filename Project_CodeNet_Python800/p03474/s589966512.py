A,B=map(int,input().split())
S=input()
a='Yes'
for i in range(A+B+1):
  if i==A:
    if S[i]!='-':
      a='No'
  else:
    if S[i]=='-':
      a='No'
print(a)