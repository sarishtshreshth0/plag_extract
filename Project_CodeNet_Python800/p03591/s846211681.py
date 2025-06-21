s=list(input())
s.append("0")
YAKI=["Y","A","K","I"]
ans=1
for i in range(4):
  if s[i] != YAKI[i]:
    ans=0
    break
if ans == 1:
  print("Yes")
else:
  print("No")