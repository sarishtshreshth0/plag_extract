s=input()
ss=int(s)
keep=0
for i in range(len(s)):
  keep+=int(s[i])
if ss%keep==0:
  print("Yes")
else:
  print("No")