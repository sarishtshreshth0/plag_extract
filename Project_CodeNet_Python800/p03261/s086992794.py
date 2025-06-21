l=[input() for _ in range(int(input()))]
for i,w in enumerate(l):
  if i:
    if l[i][0]!=l[i-1][-1] or w in l[:i]:
      exit(print('No'))
print('Yes')