N = int(input())
list1 = []
count = 0
for i in range(N):
  a = input()
  list1.append(a)
for i in range(N-1):
  if list1[i][-1] == list1[i+1][0]:
    pass
  else:
    count +=1
aaa = set(list1)
if len(aaa) == len(list1):
  pass
else:
  count+=1
if count == 0:
  print('Yes')
else:
  print('No')