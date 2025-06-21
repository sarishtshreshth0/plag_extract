n = int(input())
a = input()
cr = 0
cl = 0
ans = a
for i in range(n):
  if a[i] == "(":
    cl += 1
  elif a[i] == ")":
    cr += 1
  if cl == 0 and cr != 0:
    ans = "(" + ans
    cr -= 1
  if cl != 0 and cr != 0:
    if cr >= cl:
      cl, cr = 0,cr-cl
    else:
      cl, cr = cl-cr,0
if cl != 0:
  for i in range(cl):
    ans = ans+")"
print(ans)
