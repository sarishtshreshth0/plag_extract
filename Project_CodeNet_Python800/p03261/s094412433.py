n = int(input())

s = []
for i in range(n):
  s.append(input())
  
no = False

s_1 = s[1::]

for i, c in enumerate(s):
  if s.count(c) > 1:
    no = True
    
  if i < len(s)-1:
    c_1 = s_1[i]
    if c[-1] != c_1[0]:
      no = True
      
if no == True:
  print('No')
else:
  print('Yes')