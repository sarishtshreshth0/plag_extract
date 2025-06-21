N = int(input())
S = input()
l = 0
r = 0
for i in range(N):
  if S[i] == ')':
    if r > 0:
      r-=1
    else:
      l+=1
  else:
    r+=1
for _ in range(l):
  print('(', end='')
print(S, end='')
for _ in range(r):
  print(')', end='')