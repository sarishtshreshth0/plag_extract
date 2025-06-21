a,b,c,d = map(int,input().split())
if b < c:
  print(0)
  exit()
print(max(0, min(d,b)-max(a,c)))