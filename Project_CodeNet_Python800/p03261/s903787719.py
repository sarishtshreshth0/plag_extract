l=[input() for _ in range(int(input()))]
for i,w in enumerate(l):
  if i:
    if l[i][0]==l[i-1][-1] and w not in l[:i]:
      continue
    exit(print('No'))
print('Yes')