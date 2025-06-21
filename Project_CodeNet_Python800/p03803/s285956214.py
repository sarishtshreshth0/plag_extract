a, b = map(int, input().split())

if a==1 or b==1:
  print("Alice" if a<b
       else "Draw" if a==b
       else "Bob")
else:
  print("Alice" if a>b
       else "Draw" if a==b
       else "Bob")