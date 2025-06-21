N = int(input())
S = input()
LR = [0,0]
l = "("
r = ")"

for i in range(N):
  if S[i] == r:
    if LR[1] == 0:
      LR[0] += 1
    else:
      LR[1] -= 1
  elif S[i] == l:
    LR[1] += 1

S = l * LR[0] + S + r * LR[1]

print(S)

