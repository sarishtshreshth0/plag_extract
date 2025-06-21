N = int(input())

list_0=[]

for i in range(N):
  W = str(input())
  if W in list_0:
    print('No')
    exit()
  else:
    list_0.append(W)

for _ in range(N-1):
  if list_0[_][len(list_0[_])-1]==list_0[_+1][0]:
    pass
  else:
    print('No')
    exit()

print('Yes')