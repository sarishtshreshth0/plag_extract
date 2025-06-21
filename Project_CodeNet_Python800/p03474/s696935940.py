A,B=map(int,input().split())
s=input()
S=[s[i] for i in range(len(s))]
N=A+B+1
c=0
num={str(i) for i in range(10)}
if S[A]=='-' and len(S)==N:
  c=1
  S.pop(A)
  for i in range(N-1):
    if 1-(S[i] in num):
      c=0
if c==1:
  print('Yes')
else:
  print('No')