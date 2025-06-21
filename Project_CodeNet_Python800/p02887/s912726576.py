N=int(input())
S=list(input())
if N == 1:
  print(1)
if N>=2:
  if S[0] == S[1]:
    S[0]==" "
  for i in range(1,N):
    if S[i-1]==S[i]:
      S[i-1]=" "
  A=[]
  for i in range(N):
        if S[i]!=" ":
              A.append(S[i])
  print(len(A))