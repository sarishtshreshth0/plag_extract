n, a, b = map(int, input().split())
s = list(input())
m = 0
k = 0
for i in range(n):
 
  if s[i] == 'c':
    print('No')
  elif s[i] == 'a':
    if m < a + b:
      print('Yes')
      m += 1 
    else:
      print('No')
  elif s[i] == 'b':
    if m < a + b and k < b:
      print('Yes')
      m += 1
      k += 1
    else:
      print('No')