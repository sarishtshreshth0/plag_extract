n = int(input())
lists = [list(input()) for _ in range(n)]
lists_2 = [lists[0]]
for i in range(1,n):
  if lists[i-1][-1] == lists[i][0]:
    if lists[i] in lists_2:
      print("No")
      exit()
    else:
      lists_2.append(lists[i])
    if i == n-1:
      print("Yes")
    else:
      continue
  else:
    print("No")
    exit()