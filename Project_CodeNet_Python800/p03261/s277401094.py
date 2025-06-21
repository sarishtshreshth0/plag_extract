N = int(input())
l = [str(input())]
for i in range(N-1):
  w = str(input())
  if w in l:
    print('No')
    exit()
  elif l[-1][-1] != w[0]:
    print('No')
    exit()
  else:
    l.append(w)
print('Yes')