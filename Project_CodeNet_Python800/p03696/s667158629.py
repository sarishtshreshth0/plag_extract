from collections import deque
n = int(input())
s = input()
A = deque([])
l = 0
r = 0
for i in range(n):
  if s[i]=='(':
    A.append(s[i])
    l += 1
  else:
    if l!=0:
      A.append(s[i])
      l -=1
    else:
      A.appendleft("(")
      A.append(s[i])

for j in range(l):
  A.append(")")
  
print("".join(A))