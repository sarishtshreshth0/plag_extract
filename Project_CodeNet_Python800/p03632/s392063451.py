a,b,c,d = list(map(int,input().strip().split()))

if a <= c and d <= b:
  print(d-c)
elif a <= c and b >= c:
  print(b-c)
elif a >=c and b <=d:
  print(b-a)
elif a >=c and d >= a:
  print(d-a)

else:
  print(0)