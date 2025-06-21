N=int(input())
S=input()

new = S[0]
for i in range(1,N):
  if S[i]!=S[i-1]:new = new + S[i]
print(len(new))