a,b=map(int,input().split())
#n=int(input())
#s=input()
if a==b:
  print("Draw")
elif a>b and b!=1:
  print("Alice")
elif a>b:
  print("Bob")
elif a<b and a!=1:
  print("Bob")
else:
  print("Alice")