a, b=map(int, input().split())
nums=set([str(i) for i in range(10)])
s=input()
for x in range(a):
  if s[x] in nums:
    pass
  else:
    print('No')
    exit()
if s[a]=='-':
  pass
else:
  print('No')
  exit()
for x in range(a+1, a+1+b):
  if s[x] in nums:
    pass
  else:
    print('No')
    exit()
print('Yes')