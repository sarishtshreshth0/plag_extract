import re
a,b=input().split()
s=input()
pat ="^\d{"+a+"}-\d{"+b+"}$"
match = re.search(pat,s)
if match:
  print('Yes')
else:
  print('No')
