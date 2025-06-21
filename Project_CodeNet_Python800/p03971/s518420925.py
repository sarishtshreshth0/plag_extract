n, a, b = map(int, input().split())
bo = a + b
sl = list(input())
pa, pb = 0, 0
              
for i in range(n):
  if pa + pb < bo:
    if sl[i] == 'c':
      print('No')
    elif sl[i] == 'a':
      print('Yes')
      pa += 1
    elif sl[i] == 'b' and pb < b:
      print('Yes')
      pb += 1
    else:
      print('No')
  else:
  	print('No')