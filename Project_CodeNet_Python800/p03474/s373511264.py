f=1
a,b=list(map(int,input().split()))
s=input()
if s[a]!="-":
  f=0

for i in range(a):
  if not s[i] in "1234567890":
    f=0
for i in range(b):
  if not s[i+a+1] in "1234567890":
    f=0
if f:
  print("Yes")
else:
  print("No")