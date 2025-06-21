N=int(input())
S=input()
stack= []
ans=""
L=0
R=0

for i in range(N):
  if S[i]=="(":
    stack.append(S[i])
  else:
    if len(stack)>0:
      stack.pop()
    else:
      L += 1

R=len(stack)
ans = L * "(" + S + R * ")"

print(ans)