N = int(input())
S = input()
S = list(S)

ans = ""
for i in range(N-1):
  if S[i]==S[i+1]:
    ans+=S[i]
    
print(N-len(ans)) 