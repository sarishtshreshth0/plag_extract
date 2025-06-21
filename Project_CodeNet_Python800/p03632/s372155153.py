a,b,c,d = map(int,input().split())
if b<c or d<a:
  print(0)
elif a<=c and c<=b:
  print(min(b,d)-c)
else:
  print(min(b,d)-a)  