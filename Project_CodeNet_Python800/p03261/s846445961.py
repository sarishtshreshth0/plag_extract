N = int(input())
history = [input()]
for i in range(N-1):
  w = input()
  if w in history or history[-1][-1] != w[0]:
    print('No')
    exit()
  history.append(w)
print('Yes')