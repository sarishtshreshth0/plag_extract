N = int(input())
L = set([])
for i in range(N):
  temp = str(input())
  if i == 0:
    last = temp[-1]
    L.add(temp)
    continue
  if temp[0] != last or temp in L:
    print("No")
    exit()
  else:
    last = temp[-1]
    L.add(temp)
print("Yes")