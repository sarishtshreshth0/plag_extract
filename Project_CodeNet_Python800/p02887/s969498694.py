N=int(input())
S=input()
res=[S[0]]
for i in range(N-1):
  if(S[i]!=S[i+1]):
    res.append(S[i+1])
print(len(res))