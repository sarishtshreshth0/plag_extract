Row = int(input())
flag = True
List = []
for i in range (Row):
  List.append(input())
s_l = set(List)
if len(List) != len(s_l):
  print("No")
else:
  for i in range(Row-1):
    n = len(List[i])-1
    if List[i][n] != List[i+1][0]:
      flag = False
  if flag:
    print("Yes")
  else:
    print("No")