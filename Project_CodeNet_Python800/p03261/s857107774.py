n = int(input())
w = [ input() for i in range(n) ]
#n = 9
#w = ['basic', 'c', 'cpp', 'php', 'python', 'nadesico', 'ocaml', 'lua', 'assembly']

a = set()
a.add(w[0])
ck = 0
for i in range(1,n):
  if w[i] in a:
    break
  else:
    a.add(w[i])
  
  if w[i][0] != w[i-1][-1]:
    break

else:
  ck = 1

print('Yes' if ck else 'No')