a,b=map(int,input().split())
List = [2,3,4,5,6,7,8,9,10,11,12,13,1]
c = 0
d = 0
for i in range(13):
  if a == List[i]:
    c = i
  if b == List[i]:
    d = i
if c == d:
  print("Draw")
elif c < d:
  print("Bob")
else:
  print("Alice")