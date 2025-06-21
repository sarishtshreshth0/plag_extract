S = input()
N = len(S)

ans_1 = 0
ct = 0
for i in range(N):
  if int(S[i]) != ct:
    ans_1 += 1
  ct += 1
  ct %= 2
  
ans_2 = 0
ct = 1
for i in range(N):
  if int(S[i]) != ct:
    ans_2 += 1
  ct += 1
  ct %= 2
  
print(min(ans_1, ans_2))