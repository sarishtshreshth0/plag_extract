N = int(input())
S = input()
fused = [S[0]]
for i in range(len(S)):
  if S[i] != fused[-1]:
    fused.append(S[i])

print(len(fused))