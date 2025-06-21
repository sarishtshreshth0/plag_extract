S=input()
N=len(S)

if N%2==0:
  S1="10"*(N//2)
  count=0
  for i in range(N):
    if S[i]==S1[i]:
      count+=1
  if count >= N//2:
    print(N-count)
  else:
    print(count)
else:
  S2="10"*((N-1)//2)+"1"
  count=0
  for i in range(N):
    if S[i]==S2[i]:
      count+=1
  if count >= (N+1)//2:
    print(N-count)
  else:
    print(count)