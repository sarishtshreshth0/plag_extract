n,a,b = map(int, input().split())
s = str(input())
a_count,b_count = 0,0
for i in range(n):
  if s[i] == 'c':
    print('No')
  elif s[i] == 'a':
    if a_count+b_count < a+b:
      print('Yes')
      a_count += 1
    else:
      print('No')
  elif s[i] == 'b':
    if a_count+b_count < a+b and b_count < b:
      print('Yes')
      b_count += 1
    else:
      print('No')