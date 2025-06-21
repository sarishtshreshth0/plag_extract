N = int(input())
S = input()

sl = 0
sr = 0
slmax = 0
srmax = 0
for i in range(N):
  if(S[i] == '('):
    sl -= 1
  else:
    sl += 1
  slmax = max(slmax, sl)
for i in range(N):
  if(S[N-i-1] == '('):
    sr += 1
  else:
    sr -= 1
  srmax = max(srmax, sr)
for i in range(slmax):
  S = '(' + S
for i in range(srmax):
  S = S + ')'
print(S)