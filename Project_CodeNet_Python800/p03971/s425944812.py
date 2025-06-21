n,a,b = map(int,input().split())
s = input()
ca = 0
cb = 0
for i in range(n):
  if s[i] == 'a':    
    if ca + cb < a + b:
      ca += 1
      print('Yes')
      continue
  if s[i] == 'b':    
    if (ca + cb < a + b) and cb < b:
      cb += 1
      print('Yes')
      continue
  print('No')    