N=int(input())
history=[]
for i in range(N):
  s = input()
  if i == 0:
    history.append(s)
    continue
  if s not in history and history[-1][-1]==s[0]:
    history.append(s)
  else:
    print('No')
    exit()
print('Yes')