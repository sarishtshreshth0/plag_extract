a, b, c, d = map(int, input().split())
 
start = max(a, c)
finish = min(b, d)

if finish - start < 0:
  print(0)
else:
  print(finish - start)